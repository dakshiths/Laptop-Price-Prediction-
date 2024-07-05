from django.db import models

# predictor/models.py
from django.db import models

class LaptopFeature(models.Model):
    processor_speed = models.FloatField()
    ram_size = models.IntegerField()
    storage_capacity = models.IntegerField()
    screen_size = models.FloatField()
    weight = models.FloatField()
    predicted_price = models.FloatField()

