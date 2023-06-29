from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Item, Store


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['pk', 'name']


class ItemLeaderboardSerializer(ModelSerializer):
    top1 = SlugRelatedField(slug_field='name', queryset=Store.objects.all())
    top2 = SlugRelatedField(slug_field='name', queryset=Store.objects.all())
    top3 = SlugRelatedField(slug_field='name', queryset=Store.objects.all())
    top4 = SlugRelatedField(slug_field='name', queryset=Store.objects.all())
    top5 = SlugRelatedField(slug_field='name', queryset=Store.objects.all())

    class Meta:
        model = Item
        fields = ['pk', 'name', 'top1', 'top1Price', 'top2', 'top2Price', 'top3', 'top3Price', 'top4', 'top4Price', 'top5', 'top5Price']
