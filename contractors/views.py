from django.shortcuts import render, redirect
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
    print(driver.contractorBusiness.id)
    contractor = Contractor.objects.get(pk=driver.contractorBusiness.id)
    context = {
        'driver': driver
    }
    return render(request, 'driver_detail.html', context)


def driver_update(request, pk):
    driver = Driver.objects.get(pk=pk)
    print(request.method)
    if request.method == 'POST':
        form = updateDriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect(f'/contractors/driver_detail/{driver.pk}')
    else:
        form = updateDriverForm(instance=driver)

    context = {
        'form': form,
        'driver': driver
    }
    return render(request, 'driver_update.html', context)
# https://stackoverflow.com/questions/57328114/how-can-i-display-database-data-on-a-django-form
