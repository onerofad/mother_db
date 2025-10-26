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
    selectedStartDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    watcher_role = models.TextField()
    child_option = models.CharField(max_length=255, default='')
    rate_hour = models.CharField(max_length=255)
    email = models.ForeignKey(Register, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


