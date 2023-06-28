from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def store_profile(request):
    data = {
        'name': 'Shemsu',
        'location': 'merkato aroge tera',
    }
    return render(request, template_name='core/login.html', context={'DATA': data})


@api_view()
def store_cashier(request):
    return Response('cashier')


@api_view()
def leaderboard(request):
    return Response('leaderboard')


@api_view()
def customer_pay(request):
    return Response('core pay')