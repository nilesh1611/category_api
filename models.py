from django.db import models

# Create your models here.


class Item(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(max_length=255)

    def __str__(self):
        return self.name

