from django.urls import path
from .views import store_profile, store_cashier, leaderboard

urlpatterns = [
    path('profile', store_profile),
    path('cashier/', store_cashier),
    path('leaderboard/', leaderboard)
]
