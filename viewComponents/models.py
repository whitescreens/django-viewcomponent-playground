from django.db import models

# Create your models here.
class Fruits(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name