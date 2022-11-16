from django import forms
from contractors.models import Driver, Contractor, Vehicle, Address

class DriverForm(forms.Form):
    driverCliNumber = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Driver Cli Number"
        })
    )
    driverType = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Driver Type"
        })
    )


class updateDriverForm(forms.ModelForm):
    driverType = forms.CharField(max_length=100)
    firstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    homePhone = forms.CharField(max_length=13)

    class Meta:
        model = Driver
        fields = ("driverType", "firstName", "LastName", "homePhone")
    def save(self, commit=True):
        send = super(updateDriverForm,  self)
        if commit:
            send.save()
        return send

    