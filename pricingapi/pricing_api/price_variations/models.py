from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class PriceVariation(models.Model):
    base_price_id = models.IntegerField()
    variation = models.FloatField()
    day = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)])

    class Meta:
        db_table = 'price_variations'
