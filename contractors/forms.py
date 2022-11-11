from django import forms


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
