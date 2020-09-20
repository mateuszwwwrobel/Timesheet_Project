from django.db import models
from django.conf import settings
from django.utils import timezone 
#Create your models here.

CARS_REG = (
    ('SM16 SWF', 'SM16 SWF - White Toyota Hilux'),
    ('FL64 EBN', 'FL64 EBN - White Toyota Hilux'),
    ('WG63 LVZ', 'WG63 LVZ - Volkswagen Caddy Van'),
    ('SC16 SYZ', 'SC16 SYZ - Vauxhall Movano Flatbed Truck'),
    ('SA13 KLJ', 'SA13 KLJ - White Ford Ranger'),
    ('SJ62 RMU', 'SJ62 RMU - Black Toyota Hilux'),
    ('HG61 HGZ', 'HG61 HGZ - Blue Toyota Hilux'),
    ('SC15 MYR', 'SC15 MYR - White Land Rover Defender'),
    ('FG61 YVW', 'FG61 YVW - Grey Toyota Hilux'),
)


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    site_name =  models.CharField(max_length=40)
    duration = models.FloatField()
    contract_number = models.CharField(max_length=5, blank=True, null=True)
    description = models.TextField()
    car_reg = models.CharField(max_length=20, blank=True, null=True, choices=CARS_REG)


    def __str__(self):
        return str(self.user) +' - ' + str(self.date)



