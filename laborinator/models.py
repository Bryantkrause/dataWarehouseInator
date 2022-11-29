from django.db import models

# Create your models here.


class Labor(models.Model):
    voucher_number = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.IntegerField()
    hours = models.IntegerField()

    class Meta:
        app_label = 'laborinator'  # name of app

    def __str__(self):
        return self.voucher_number
