from django.db import models

# Create your models here.
# https://stackoverflow.com/questions/35609509/django-migrations-with-multiple-databases
# https://dev.to/minhvuong1/how-to-set-up-multiple-databases-on-django-1c76

# use this one
# https://stackoverflow.com/questions/57676143/using-multiple-databases-with-django


class Content(models.Model):
    app_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.app_name
