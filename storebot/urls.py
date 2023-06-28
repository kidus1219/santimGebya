from django.urls import path
from .views import webhook_handler
from .const import BOT_TOKEN

urlpatterns = [
    path(f'{BOT_TOKEN}/webhook/', webhook_handler),
]
