from django.urls import path
from .views import store_profile, store_cashier, leaderboard, generate_qr

urlpatterns = [
    path('profile/', store_profile),
    path('cashier/', store_cashier),
    path('leaderboard/', leaderboard),
    path('generate-qr/', generate_qr)
]
