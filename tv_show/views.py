from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def films_view(request):
    films = models.TvShow.objects.all()
    return render(request, 'films/films.html', {'films': films})

def films_detail_view(request, id):
    films_id = get_object_or_404(models.TvShow, id=id)
    return render(request, 'films/films_detail.html', {'films_id': films_id})


def create_films(request):
    method = request.method
    if method == 'POST':
        form = forms.FilmsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Succesfully!')
    else:
        form = forms.FilmsForm()

    return render(request, 'films/crud/add_films.html', {'form': form})

def delete_films(request, id):
    films_id = get_object_or_404(models.TvShow, id=id)
    films_id.delete()
    return HttpResponse('Succesfully deleted!')


def update_films(request, id):
    films_id = get_object_or_404(models.TvShow, id=id)
    if request.method == 'POST':
        form = forms.FilmsForm(instance=films_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Succesfully add!')
    else:
        form = forms.FilmsForm(instance=films_id)

    context = {
        'form': form,
        'films_id': films_id
    }
    return render(request, 'films/crud/update_films.html', context)