from django.db import models

# Create your models here.


class BasePrice(models.Model):
    room_type_id = models.IntegerField()
    value = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    # allow to set a custom table name in database, else it will be [appname]_[modelname]
    class Meta:
        db_table = 'base_prices'
