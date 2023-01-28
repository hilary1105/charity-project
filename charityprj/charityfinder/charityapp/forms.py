import charity.models
from django import forms


class charityfinder(forms.ModelForm):
    class Meta:
        model = charityapp
        fields = "__all__"
