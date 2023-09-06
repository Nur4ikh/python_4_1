from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):

    USER_TYPE = (
        ('admin', 'admin'),
        ('super_admin', 'admin_admin'),
        ('client', 'client'),
        ('vipclient', 'vipclient'),
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
    user_type = models.CharField(max_length=100, choices=USER_TYPE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    phone_number = models.CharField(max_length=13)
    maried = models.CharField(max_length=7, choices=MARIED)
    gender = models.CharField(max_length=7, choices=GENDER)
    children = models.CharField(max_length=3, choices=CHILDREN)
    age = models.PositiveIntegerField(default=18)
    about_me = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    hobby = models.CharField(max_length=20)
    favorite_food = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    favorite_film = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user_type

