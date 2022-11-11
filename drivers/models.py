# from django.db import models

# # Create your models here.


# class Driver(models.Model):
#     driverCliNumber = models.IntegerField(primary_key=True)
#     contractorBusiness = models.ForeignKey(
#         'Contractor', on_delete=models.CASCADE)
#     driverType = models.CharField(max_length=100)
#     firstName = models.CharField(max_length=100)
#     LastName = models.CharField(max_length=100)
#     homePhone = models.CharField(max_length=13)
#     cellPhone = models.CharField(max_length=13)
#     startDate = models.DateField()
#     RegistrationExpires = models.DateField()
#     terminated = models.BooleanField()
#     terminatedDate = models.DateField(null=True, blank=True)
#     licenseNumber = models.CharField(max_length=100)
#     last_modified = models.DateTimeField(auto_now=True)
#     # image = models.FilePathField(path="/img")


# class Contractor(models.Model):
#     startDate = models.DateField(default='2022-01-01')
#     contractorBusinessName = models.CharField(
#         max_length=100, default='TotallyRealContractor')
#     firstName = models.CharField(max_length=100, default='Bob')
#     lastName = models.CharField(max_length=100, default='Builder')
#     addressNumber = models.CharField(max_length=100, default='123')
#     addressLocation = models.CharField(max_length=100, default='Street')
#     city = models.CharField(max_length=100, default='Real City')
#     state = models.CharField(max_length=100, default='CA')
#     zip = models.CharField(max_length=100, default='12345')
#     last_modified = models.DateTimeField(auto_now=True)
