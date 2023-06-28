import json
from django.http import JsonResponse
from .main import StoreBotApplication


async def webhook_handler(request):
    try:
        await StoreBotApplication.instance.handle(json.loads(request.body.decode()))
    except Exception as e:
        print('Xx storebot.views.webhook_handler Exception ', e)
    return JsonResponse({'result': 'ok'})
