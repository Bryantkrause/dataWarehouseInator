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

    class Meta:
        model = Driver
        fields = '__all__'

    def save(self, commit=True):
        send = super(updateDriverForm,  self)
        if commit:
            send.save()
        return send
