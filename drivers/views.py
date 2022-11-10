from django.shortcuts import render
from drivers.models import Driver, Contractor
from .forms import DriverForm


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


def contractor_index(request):
    contractors = Contractor.objects.all().order_by('-startDate')
    context = {
        "contractors": contractors,
    }
    return render(request, "contractor_index.html", context)


def contractor_detail(request, contractor):
    drivers = Driver.objects.filter(
        contractor__name__contains=contractor
    ).order_by(
        '-startDate'
    )
    context = {
        "contractor": contractor,
        'drivers': drivers
    }
    return render(request, 'contractor_detail.html', context)


def add_driver(request, pk):
    contractor = Contractor.objects.get(pk=pk)
    drivers = Driver.objects.filter(contractor=contractor)

    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = Driver(
                driverCliNumber=form.cleaned_data["driverCliNumber"],
                driverType=form.cleaned_data["driverType"],
                contractor=contractor
            )



    context = {
        "contractor": contractor,
        'drivers': drivers
    }
    return render(request, 'add_driver.html', context)
