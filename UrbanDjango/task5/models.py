from django.db import models

# Create your models here.

class UserRegister(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=8)
    repeat_password = models.CharField(max_length=8)
    age = models.CharField(max_length=3)


    def __str__(self):
        return self.username
