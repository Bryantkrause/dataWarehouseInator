from django.shortcuts import render
from drivers.models import Driver


def driver_index(request):
    driver = Driver.objects.all()
    context = {
        'driver': driver
    }
    return render(request, 'driver_index.html', context)


def driver_detail(request, pk):
    driver = Driver.objects.get(pk=pk)
    context = {
        'driver': driver
    }
    return render(request, 'driver_detail.html', context)
