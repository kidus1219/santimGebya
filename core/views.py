from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Store, Item
from .serializers import ItemSerializer, ItemLeaderboardSerializer

@api_view()
def store_profile(request):
    items = Item.objects.all()
    data = {
        'name': 'Shemsu',
        'location': 'merkato aroge tera',
    }
    print(data)
    return render(request, template_name='core/profile.html', context={'DATA': data})


@api_view()
def store_cashier(request):
    items = Item.objects.all()
    data = {
        'qrApi': "http://localhost:8000/generate-qr/",
        'items': ItemSerializer(items, many=True).data
    }
    print(data)
    return render(request, template_name='core/cashier.html', context={'DATA': data})


@api_view()
def leaderboard(request):
    items = Item.objects.all()
    data = {
        'items': ItemLeaderboardSerializer(items, many=True).data
    }
    print(data)
    return render(request, template_name='core/leaderboard.html', context={'DATA': data})


@api_view(['POST'])
def generate_qr(request):
    print('hi')
    return Response('core pay')