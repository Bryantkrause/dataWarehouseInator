from django.db import models

# Create your models here.

class Driver(models.Model):
    driverCliNumber = models.IntegerField(primary_key=True)
    driverType = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    homePhone = models.CharField(max_length=100)
    cellPhone = models.CharField(max_length=100)
    startDate = models.DateField()
    RegistrationExpires = models.DateField()
    terminated = models.BooleanField()
    terminatedDate = models.DateField()
    licenseNumber = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
