import asyncio

# bind = "0.0.0.0:7000"
bind = "127.0.0.1:7000"
# bind = 'unix:///tmp/nginx.socket'
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"
# preload_app = True


def when_ready(server):
    print('---------- READY -----------------')  # , txAll())
    # open('/tmp/app-initialized', 'w').close()


def post_fork(server, worker):
    print('---------- POST FORK -----------------')  # , txAll())


def post_worker_init(worker):
    print('---------- POST WORKER INIT -----------------')  # , txAll())
    loop = asyncio.get_event_loop()
    # from customerbot.main import CustomerBotApplication
    from storebot.main import StoreBotApplication
    # loop.run_until_complete(CustomerBotApplication().run())
    # loop.run_until_complete(StoreBotApplication().run())
#