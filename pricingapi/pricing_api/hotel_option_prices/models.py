from django.db import models

# Create your models here.


class HotelOptionPrice(models.Model):
    hotel_option_id = models.IntegerField()
    value = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'hotel_option_prices'
