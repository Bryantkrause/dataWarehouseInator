from django.db import models

# Create your models here.
# https://stackoverflow.com/questions/35609509/django-migrations-with-multiple-databases
# https://dev.to/minhvuong1/how-to-set-up-multiple-databases-on-django-1c76

# use this one
# https://stackoverflow.com/questions/57676143/using-multiple-databases-with-django


class Expense(models.Model):
    voucher_number = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.IntegerField()

    class Meta:
        # app_label helps django to recognize your db
        app_label = 'expensinator'

    def __str__(self):
        return self.voucher_number
