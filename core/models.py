from django.db import models


# Create your models here.
class Item(models):
    name = models.CharField(max_length=15)


class Store(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "Store"

