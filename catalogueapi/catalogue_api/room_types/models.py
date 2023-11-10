from django.db import models

# Create your models here.


class RoomType(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    # allow to set a custom table name in database, else it will be [appname]_[modelname]
    class Meta:
        db_table = 'room_types'
