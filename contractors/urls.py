from django.urls import path
from . import views

app_name = 'contractors'
urlpatterns = [
    path("", views.contractor_index, name="contractor_index"),
    path("add/", views.contractor_add, name="contractor_add"),
    path("driver_add/<int:pk>/", views.driver_add, name="driver_add"),
    path("<int:pk>/", views.contractor_detail, name="contractor_detail"),
    path("table/", views.contractor_table, name="contractor_table"),
    path("detailtable/<int:pk>", views.contractor_detailTable,
         name="contractor_detailTable"),
    path("driver_detail/<int:pk>",
         views.driver_detail, name="driver_detail"),
    path("driver_update/<int:pk>/update",
         views.driver_update, name="driver_update"),
]
# https://medium.com/@9cv9official/how-to-set-up-your-homepage-with-django-ae21f439c8a3
