from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    name=models.CharField(max_length=1000)

class Message(models.Model):
    value=models.CharField(max_length=1000000)
    date=models.DateTimeField(default=datetime.now,blank=True)  
    user=models.CharField(max_length=1000000)
    room=models.CharField(max_length=1000000)
    def save(self, *args, **kwargs):
        self.date += timezone.timedelta(hours=2)
        super().save(*args, **kwargs)