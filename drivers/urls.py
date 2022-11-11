from django.urls import path
from . import views

urlpatterns = [
    path("", views.driver_index, name="driver_index"),
    path("<int:pk>/", views.driver_detail, name="driver_detail"),
]
