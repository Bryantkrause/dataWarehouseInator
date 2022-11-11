from django.urls import path
from . import views

urlpatterns = [
    path("", views.contractor_index, name="contractor_index"),
    path("<int:pk>/", views.contractor_detail, name="contractor_detail"),
]
