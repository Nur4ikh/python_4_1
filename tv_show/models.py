from django.db import models

# Create your models here.
class TvShow(models.Model):
    GENRE = (
        ('Драма', 'Драма'),
        ('Триллер', 'Триллер'),
        ('Шоу', 'Шоу'),
        ('Концерт', 'Концерт'),
        ('Ужасы', 'Ужасы'),
        ('Детектив', 'Детектив'),
        ('Фантастический', 'Фантастический'),
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    price = models.CharField(max_length=8, null=True)
    year = models.CharField(max_length=15, null=True)
    time = models.IntegerField()
    reviews = models.CharField(max_length=300)
    country = models.CharField(max_length=15)
    genre = models.CharField(max_length=30, choices=GENRE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title