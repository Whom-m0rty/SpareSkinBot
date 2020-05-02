from django.db import models

# Create your models here.


class User(models.Model):
    chat_id = models.IntegerField()
    orders = models.TextField(default=':')