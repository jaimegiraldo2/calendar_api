from django.db import models

class Event(models.Model):

    """ simple model of an event app taking only 
    name of the event, start date it could include the time,
    end date also you could put the time, color and the
    details of the event"""

    name = models.CharField(max_length=140)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    details = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
