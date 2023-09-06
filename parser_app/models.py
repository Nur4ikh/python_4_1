from django.db import models

class FilmParser(models.Model):
    title_url = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title_text
