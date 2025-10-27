from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    about = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    picture = models.TextField(max_length=255, default='')

    def __str__(self):
        return self.firstname
    
class MakeRequest(models.Model):
    selectedStartDate = models.CharField(max_length=255, default='')
    startTime = models.CharField(max_length=255, default='')
    endTime = models.CharField(max_length=255, default='')
    watcher_role = models.TextField()
    child_option = models.CharField(max_length=255, default='')
    rate_hour = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.email
    
class Support(models.Model):
    email = models.CharField(max_length=255)
    helpText = models.TextField()

    def __str__(self):
        return self.helpText


