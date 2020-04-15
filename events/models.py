from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=140)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    details = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
