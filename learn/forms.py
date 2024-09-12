from django import forms
from .models import ContactModel


class ContactModelForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ["first_name", "last_name", "email", "message", "details"]
