from django.db import models
#from users_api.users.models import User

class Bookings(models.Model):
    room_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    love_pack = models.BooleanField()
    breakfast = models.BooleanField()
    user_id = models.IntegerField() # i have my doubts about this line

    # allow to set a custom table name in database, else it will be [appname]_[modelname]
    class Meta:
        db_table = 'bookings'

    # def save(self, *args, **kwargs):
    #     """
    #     Override the save method of the model to add the owner
    #     """
    #     start_date = self.start_date
    #     end_date = self.end_date
    #     love_pack = self.love_pack
    #     breakfast = self.breakfast
    #     super().save(*args, **kwargs)

