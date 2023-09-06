from django.db import models

# Create your models here.
class Cars(models.Model):


    TYPE_CAR = (
        ('old', 'old'),
        ('sport', 'sport'),
        ('gruz', 'gruz')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    description = models.TextField()
    color = models.CharField(max_length=100)
    type_car = models.CharField(max_length=100, choices=TYPE_CAR)
    url_car = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title