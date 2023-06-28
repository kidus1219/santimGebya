import asyncio
import json
import os
import threading
from django.http import JsonResponse
from .main import CustomerBotApplication


async def webhook_handler(request):
    # print('---------- IN REQUEST -----------------', txAll())
    if CustomerBotApplication.instance is None:
        print('bot init')
        await CustomerBotApplication().run()
    else:
        try:
            print('view started', os.getpid())
            data = json.loads(request.body.decode())
            await CustomerBotApplication.instance.handle(data)
            print('view finished', id(asyncio.get_running_loop()))
        except Exception as e:
            print('parsing data failed ', e)
    return JsonResponse({'result': 'ok'})


def txAll():
    result = ""
    for i, t in enumerate(threading.enumerate()):
        result += f"{i + 1} => {t.name} id -> {id(t)} .. || .. "

    result += "\ncurrent = " + str(threading.current_thread().name) + " id -> " + str(
        id(threading.current_thread())) + "\n/////////////\n/////////////"
    return result
