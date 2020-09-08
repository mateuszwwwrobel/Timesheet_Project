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


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=3, choices=DAY_OF_THE_WEEK)
    duration = models.FloatField()
    contract_number = models.CharField(max_length=5)
    description = models.TextField()
    car_reg = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return str(self.user) +' - ' + self.day_of_the_week



class UserTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    all_tasks = models.ManyToManyField(Task)
