from django.db import models


class Store(models.Model):
    ownerId = models.CharField(max_length=64)
    name = models.CharField(max_length=15)
    merchantId = models.CharField(max_length=100)
    location = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "Store"


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=15)
    top1 = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='top1')
    top1Price = models.CharField(max_length=15, null=True, blank=True, )
    top2 = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='top2')
    top2Price = models.CharField(max_length=15, null=True, blank=True, )
    top3 = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='top3')
    top3Price = models.CharField(max_length=15, null=True, blank=True, )
    top4 = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='top4')
    top4Price = models.CharField(max_length=15, null=True, blank=True, )
    top5 = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='top5')
    top5Price = models.CharField(max_length=15, null=True, blank=True, )

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "Item"
