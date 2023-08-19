from django.shortcuts import render, get_object_or_404
from . import models

def films_view(request):
    films = models.TvShow.objects.all()
    return render(request, 'films/films.html', {'films': films})

def films_detail_view(request, id):
    films_id = get_object_or_404(models.TvShow, id=id)
    return render(request, 'films/films_detail.html', {'films_id': films_id})
