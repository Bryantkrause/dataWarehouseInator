from django.shortcuts import render
from contractors.models import Driver, Contractor, Vehicle, Address
from .forms import DriverForm
# Create your views here.


def contractor_index(request):
    contractors = Contractor.objects.all().order_by('-startDate')
    context = {
        "contractors": contractors,
    }
    return render(request, "contractor_index.html", context)


def contractor_detail(request, pk):
    contractor = Contractor.objects.get(pk=pk)
    

    drivers = Driver.objects.filter(
        contractorBusiness=pk
    )
    context = {
        'contractor': contractor,
        'drivers': drivers
    }
    return render(request, 'contractor_detail.html', context)


def driver_detail(request, pk):
    driver = Driver.objects.get(pk=pk)
    context = {
        'driver': driver
    }
    return render(request, 'driver_detail.html', context)
