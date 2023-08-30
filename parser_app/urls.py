from django.urls import path
from . import views

urlpatterns = [
    path('start_p/', views.ParserFormView.as_view(), name='start_p'),
    path('film_list/', views.FilmListView.as_view(), name='film_list'),
]