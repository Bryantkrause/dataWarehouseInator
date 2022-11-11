from django.contrib import admin
from contractors.models import Driver, Contractor, Address, Vehicle
# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


class VehicleAdmin(admin.ModelAdmin):
    pass


class ContractorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Driver, DriverAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Contractor, ContractorAdmin)
