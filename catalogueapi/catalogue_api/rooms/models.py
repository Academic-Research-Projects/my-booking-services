from django.db import models

# Create your models here.


class Room(models.Model):
    hotel_id = models.IntegerField()
    number = models.IntegerField()
    room_type_id = models.IntegerField()

    # allow to set a custom table name in database, else it will be [appname]_[modelname]
    class Meta:
        db_table = 'rooms'
