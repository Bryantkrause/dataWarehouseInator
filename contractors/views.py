from django.shortcuts import render
from contractors.models import Driver, Contractor
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
