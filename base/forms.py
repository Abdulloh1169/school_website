from django import forms
from django.forms import ModelForm
from . import models


class ContactAdminForm(ModelForm):
    class Meta:
        model=models.MailToAdmin
        exclude = ['checked']