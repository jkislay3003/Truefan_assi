from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


# Create your models here.
