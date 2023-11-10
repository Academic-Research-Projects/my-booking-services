from django.db import models

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    # allow to set a custom table name in database, else it will be [appname]_[modelname]
    class Meta:
        db_table = 'hotels'
