from django.shortcuts import render
from contractors.models import Driver, Contractor, Vehicle, Address
from contractors.forms import updateDriverForm

# Create your views here.


def contractor_index(request):
    contractors = Contractor.objects.all().order_by('-startDate')
    context = {
        "contractors": contractors,
    }
    return render(request, "contractor_index.html", context)


def contractor_table(request):
    contractors = Contractor.objects.all().order_by('-startDate')
    context = {
        "contractors": contractors,
    }
    return render(request, "contractor_table.html", context)


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


def contractor_detailTable(request, pk):
    contractor = Contractor.objects.get(pk=pk)

    drivers = Driver.objects.filter(
        contractorBusiness=pk
    )
    context = {
        'contractor': contractor,
        'drivers': drivers
    }
    return render(request, 'contractor_detailTable.html', context)


def driver_detail(request, pk):

    driver = Driver.objects.get(pk=pk)
    context = {
        'driver': driver
    }
    return render(request, 'driver_detail.html', context)


def driver_update(request, pk):

    if request.method == 'POST':
        form = updateDriverForm(request.POST)
        if form.is_valid():
            send = form.save(commit=False)
            send.save()
    else:
        form = updateDriverForm()
    driver = Driver.objects.get(pk=pk)
    context = {
        'form': form,
        'driver': driver
    }
    return render(request, 'driver_update.html', context)
# https://stackoverflow.com/questions/57328114/how-can-i-display-database-data-on-a-django-form
