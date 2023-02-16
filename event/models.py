from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        constraints = [
            models.UniqueConstraint(fields=["name"], name="uniqueName")
        ]
    
    

class Event(models.Model):
    name = models.CharField(max_length=200)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField('planned date')
    date = models.DateTimeField('planned date')
    attendees= models.IntegerField
    def __str__(self) -> str:
        return self.name
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
