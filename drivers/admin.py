from django.contrib import admin
from drivers.models import Driver, Contractor
# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    pass


class ContractorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Driver, DriverAdmin)
admin.site.register(Contractor, ContractorAdmin)
