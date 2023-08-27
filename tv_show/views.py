from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class TvshowView(generic.ListView):
    template_name = 'films/films.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()
class TvshowDetail(generic.DetailView):
    template_name = 'films/films_detail.html'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get("id")
        return get_object_or_404(models.TvShow, id=tvshow_id)
class CreateTvshowView(generic.CreateView):
    template_name = 'films/crud/add_films.html'
    form_class = forms.FilmsForm
    queryset = models.TvShow.objects.all()
    success_url = '/reviews/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTvshowView, self).form_valid(form=form)
class DeleteTvshowView(generic.DeleteView):
    template_name = 'films/crud/confirm_delete.html'
    success_url = '/films/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)


class UpdateTvshowView(generic.UpdateView):
    template_name = 'films/crud/update_films.html'
    form_class = forms.FilmsForm
    success_url = '/films/'

    def get_object(self, **kwargs):
        films_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=films_id)

    def form_valid(self, form):
        return super(UpdateTvshowView, self).form_valid(form=form)

class Search(generic.ListView):
    template_name = "films/films.html"
    context_context_object_name = "films"
    paginate_by = 5

    def get_queryset(self):
        return models.TvShow.objects.filter(
            title__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class CreateFilmView(generic.CreateView):
    template_name = 'films/Reviews.html'
    form_class = forms.FilmViewForm
    queryset = models.Reviews.objects.all()
    success_url = '/reviews/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateFilmView, self).form_valid(form=form)

# def films_view(request):
#     films = models.TvShow.objects.all()
#     return render(request, 'films/films.html', {'films': films})
#
# def films_detail_view(request, id):
#     films_id = get_object_or_404(models.TvShow, id=id)
#     return render(request, 'films/films_detail.html', {'films_id': films_id})
#
#
# def create_films(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.FilmsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Succesfully!')
#     else:
#         form = forms.FilmsForm()
#
#     return render(request, 'films/crud/add_films.html', {'form': form})
#
# def delete_films(request, id):
#     films_id = get_object_or_404(models.TvShow, id=id)
#     films_id.delete()
#     return HttpResponse('Succesfully deleted!')
#
#
# def update_films(request, id):
#     films_id = get_object_or_404(models.TvShow, id=id)
#     if request.method == 'POST':
#         form = forms.FilmsForm(instance=films_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Succesfully add!')
#     else:
#         form = forms.FilmsForm(instance=films_id)
#
#     context = {
#         'form': form,
#         'films_id': films_id
#     }
#     return render(request, 'films/crud/update_films.html', context)