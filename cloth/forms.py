from django import forms
from . import models


class StatusOrderForm(forms.ModelForm):
    class Meta:
        model = models.StatusOrder
        fields = "__all__"
