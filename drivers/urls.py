from django.urls import path
from . import views

urlpatterns = [
    path("", views.driver_index, name="driver_index"),
    path("<contractor>", views.driver_index, name="contractor_index"),
    path("<int:pk>/", views.driver_detail, name="driver_detail"),
    path("<int:pk>/", views.contractor_detail, name="contractor_detail"),
]
