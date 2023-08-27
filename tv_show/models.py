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

class Rating(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    Stars = models.ForeignKey(TvShow, on_delete=models.CASCADE,
                              related_name='comment_object')
    Text = models.CharField(max_length=100, choices=RATING, null=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Text


class Reviews(models.Model):
    stars = ((i, '*' * i) for i in range(1, 6))
    comment = models.CharField('Комментарий', max_length=500, null=True)
    choice_film = models.ForeignKey(TvShow, on_delete=models.CASCADE, related_name='reviews', null=True)
    rate = models.IntegerField('Оценка', choices=stars, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment
