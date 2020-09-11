from django.db import models
from django.conf import settings
import datetime

#Create your models here.

DAY_OF_THE_WEEK = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
)

CARS_REG = (
    ('SM16 SWF', 'SM16 SWF - Richards (White Toyota Hilux)'),
    ('FL64 EBN', 'FL64 EBN - Scotts (White Toyota Hilux)'),
    ('WG63 LVZ', 'WG63 LVZ - Volkswagen Caddy Van'),
    ('SC16 SYZ', 'SC16 SYZ - Vauxhall Movano Flatbed Truck'),
    ('SA13 KLJ', 'SA13 KLJ - Daniels (White Ford Ranger'),
    ('SJ62 RMU', 'SJ62 RMU - Matts (Black Toyota Hilux'),
    ('HG61 HGZ', 'HG61 HGZ - Tims (Blue Toyota Hilux)'),
    ('SC15 MYR', 'SC15 MYR - White Land Rover Defender'),
    ('XXXX ???', 'XXXX ??? - Alexs (Grey Toyota Hilux)'),
)



class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=3, choices=DAY_OF_THE_WEEK)
    site_name =  models.CharField(max_length=40)
    duration = models.FloatField()
    contract_number = models.CharField(max_length=5, blank=True, null=True)
    description = models.TextField()
    car_reg = models.CharField(max_length=20, blank=True, null=True, choices=CARS_REG)


    def __str__(self):
        return str(self.user) +' - ' + self.day_of_the_week



class UserTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    all_tasks = models.ManyToManyField(Task)
