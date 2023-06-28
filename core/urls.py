from django.urls import path
from .views import store_profile

urlpatterns = [
    path('', store_profile)
]
