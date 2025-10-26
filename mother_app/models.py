from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=255)
    lastane = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    about = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    picture = models.TextField(max_length=255, default='')

    def __str__(self):
        return self.firstname


