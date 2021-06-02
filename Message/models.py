from django.db import models

from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.CharField(max_length=250)
    receiver = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    subject = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
