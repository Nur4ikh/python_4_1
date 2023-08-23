from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.films_view, name='films'),
    path('films/<int:id>/', views.films_detail_view, name='films_detail'),
    path('films/<int:id>/delete/', views.delete_films, name='films_delete'),
    path('films/<int:id>/update/', views.update_films, name='films_update'),
    path('add-films/', views.create_films, name='add_films'),
]