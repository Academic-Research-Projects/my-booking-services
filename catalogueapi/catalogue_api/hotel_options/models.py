from django.db import models

# Create your models here.


class HotelOption(models.Model):
    class OptionType(models.TextChoices):
        PARKING_SLOT = 'PS'
        BABY_BED = 'BB'

    hotel_id = models.IntegerField()
    number = models.IntegerField()
    option_type = models.CharField(max_length=2, choices=OptionType.choices)

    class Meta:
        db_table = 'hotel_options'
