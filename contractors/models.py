from django.db import models

# Create your models here.

# https://realpython.com/get-started-with-django-1/ go here


class Contractor(models.Model):
    startDate = models.DateField(default='2022-01-01')
    contractorBusinessName = models.CharField(
        max_length=100, default='TotallyRealContractor')
    firstName = models.CharField(max_length=100, default='Bob')
    lastName = models.CharField(max_length=100, default='Builder')
    address_id = models.ForeignKey(
        'Address', on_delete=models.CASCADE
    )
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contractorBusinessName


class Driver(models.Model):
    driverCliNumber = models.IntegerField(primary_key=True)
    contractorBusiness = models.ForeignKey(
        'Contractor', on_delete=models.CASCADE)
    driverType = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    homePhone = models.CharField(max_length=13)
    cellPhone = models.CharField(max_length=13)
    startDate = models.DateField()
    dateOfBirth = models.DateField()
    RegistrationExpires = models.DateField()
    emergencyContactFirstName = models.CharField(
        max_length=100, default='FirstName')
    emergencyContactLastName = models.CharField(
        max_length=100, default='LastName')
    emergencyPhone = models.CharField(max_length=13, default='310-987-1327')
    terminated = models.BooleanField()
    terminatedDate = models.DateField(null=True, blank=True)
    licenseNumber = models.CharField(max_length=100)
    licenseClass = models.CharField(max_length=13)
    last_modified = models.DateTimeField(auto_now=True)
    address_id = models.ForeignKey(
        'Address', on_delete=models.CASCADE, default=None
    )
    vehicle_id = models.ForeignKey(
        'Vehicle', on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.firstName


class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=100)
    vehicleYear = models.IntegerField()
    vehicleMake = models.CharField(max_length=100)
    vinNumber = models.CharField(max_length=100)
    licensePlate = models.CharField(max_length=100)
    combinedVehicleWeight = models.IntegerField()
    registrationExires = models.DateField()

    def __str__(self):
        return self.vinNumber


class Address(models.Model):
    addressNumber = models.CharField(max_length=100, default='123')
    addressLocation = models.CharField(max_length=100, default='Street')
    city = models.CharField(max_length=100, default='Real City')
    state = models.CharField(max_length=100, default='CA')
    zip = models.CharField(max_length=100, default='12345')

    def __str__(self):
        return self.addressNumber + ' ' + self.addressLocation + " \n\n " + self.city + ' ' + self.state + ' ' + self.zip
