from django.db import models

class Bagan(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    wood_type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    production_days = models.IntegerField()

    def __str__(self):
        return self.name