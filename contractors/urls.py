from django.urls import  path
from . import views

app_name = 'contractors'
urlpatterns = [
    path("", views.contractor_index, name="contractor_index"),
    path("<int:pk>/", views.contractor_detail, name="contractor_detail"),
    path("driver_detail/<int:pk>",
         views.driver_detail, name="driver_detail"),
]
# https://medium.com/@9cv9official/how-to-set-up-your-homepage-with-django-ae21f439c8a3
