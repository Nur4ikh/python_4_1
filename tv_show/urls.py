from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.films_view, name='films'),
    path('films/<int:id>/', views.films_detail_view, name='films_detail')
]