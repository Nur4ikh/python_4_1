from django import forms
from . import models

class FilmsForm(forms.ModelForm):
    class Meta:
        model = models.TvShow
        fields = '__all__'

class FilmViewForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'
