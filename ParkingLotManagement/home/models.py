from django.db import models
import datetime
import time
# Create your models here.


class parkingSpots(models.Model):
    owner_name = models.CharField(max_length=122,blank=True)
    vehicle_type = models.CharField(max_length=122,blank=True)
    vehicle_no = models.CharField(max_length=122,blank=True)
    row_no = models.SmallIntegerField()
    pos_no = models.SmallIntegerField()
    occupancy = models.SmallIntegerField()
    in_time = models.TimeField()
