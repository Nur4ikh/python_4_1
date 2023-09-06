from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

USER_TYPE = (
    ('admin', 'admin'),
    ('super_admin', 'admin_admin'),
    ('client', 'client'),
    ('vipclient', 'vipclient'),
    ('admin', 'admin')
)
MARIED = (
    ('Да', 'Да'),
    ('Нет', 'Нет')
)
GENDER = (
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский')
)
CHILDREN = (
    ('Да', 'Да'),
    ('Нет', 'Нет')
)


class CustomUserRegistrations(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    name = forms.CharField(required=True)
    image = forms.ImageField(required=True)
    phone_number = forms.CharField(required=True)
    maried = forms.ChoiceField(choices=MARIED, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    children = forms.ChoiceField(choices=CHILDREN, required=True)
    age = forms.IntegerField(required=False)
    about_me = forms.TextInput()
    country = forms.CharField(required=False)
    city = forms.CharField(required=False)
    address = forms.CharField(required=False)
    hobby = forms.CharField(required=False)
    favorite_food = forms.CharField(required=False)
    language = forms.CharField(required=False)
    education = forms.CharField(required=False)
    profession = forms.CharField(required=False)
    height = forms.IntegerField(required=False)
    weight = forms.IntegerField(required=False)
    favorite_film = forms.CharField(required=False)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "user_type",
            "name",
            "image",
            "phone_number",
            "maried",
            "gender",
            "children",
            "age",
            "about_me",
            "country",
            "city",
            "address",
            "hobby",
            "favorite_food",
            "language",
            "education",
            "profession",
            "height",
            "weight",
            "favorite_film",
        )

    def save(self, commit=True):
        user = super(CustomUserRegistrations, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
