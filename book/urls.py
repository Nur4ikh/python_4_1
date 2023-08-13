from django.urls import path
from . import views
urlpatterns = [
    path('book_page/', views.book_view, name='book'),
]