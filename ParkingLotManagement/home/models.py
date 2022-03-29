from django.db import models
import datetime
# Create your models here.


class searching(models.Model):
    owner_name = models.CharField(max_length=122)
    vehicle_type = models.CharField(max_length=122)
    vehicle_no = models.CharField(max_length=122)
    row_no = models.SmallIntegerField()
    pos_no = models.SmallIntegerField()
    occupancy = models.SmallIntegerField()
    in_time = models.TimeField(datetime.time)
