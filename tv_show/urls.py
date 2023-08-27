from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.TvshowView.as_view(), name='films'),
    path('films/<int:id>/', views.TvshowDetail.as_view(), name='films_detail'),
    path('films/<int:id>/delete/', views.DeleteTvshowView.as_view(), name='films_delete'),
    path('films/<int:id>/update/', views.UpdateTvshowView.as_view(), name='films_update'),
    path('add-films/', views.CreateTvshowView.as_view(), name='add_films'),
    path('search/', views.Search.as_view(), name='search'),
    path('reviews/', views.CreateFilmView.as_view(), name='reviews'),

]