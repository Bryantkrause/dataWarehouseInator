from django.shortcuts import render
from drivers.models import Driver, Contractor


def driver_index(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request, 'driver_index.html', context)


def driver_detail(request, pk):
    driver = Driver.objects.get(pk=pk)
    context = {
        'driver': driver
    }
    return render(request, 'driver_detail.html', context)


def blog_index(request):
    contractors = Contractor.objects.all().order_by('-created_on')
    context = {
        "contractors": contractors,
    }
    return render(request, "contractor_index.html", context)
