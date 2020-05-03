from django.db import models

# Create your models here.


class User(models.Model):
    chat_id = models.IntegerField()
    orders = models.TextField(default=':')


class Message(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()