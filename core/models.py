from django.db import models




class Store(models.Model):
    ownerId = models.CharField(max_length=64)
    name = models.CharField(max_length=15)
    merchantId = models.CharField(max_length=100)
    location = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "Store"


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=15)
    top1 = models.OneToOneField(Store, on_delete=models.SET_NULL, null=True, related_name='top1')
    top2 = models.OneToOneField(Store, on_delete=models.SET_NULL, null=True, related_name='top2')
    top3 = models.OneToOneField(Store, on_delete=models.SET_NULL, null=True, related_name='top3')
    top4 = models.OneToOneField(Store, on_delete=models.SET_NULL, null=True, related_name='top4')
    top5 = models.OneToOneField(Store, on_delete=models.SET_NULL, null=True, related_name='top5')

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "Item"
