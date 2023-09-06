from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('men_shoes/', views.MenShoes.as_view(), name='men_shoes'),
    path('women_shoes/', views.WomenShoes.as_view(), name='women_shoes'),
    path('kids_shoes/', views.KidsShoes.as_view(), name='kids_shoes'),
    path('teenage_shoes/', views.TeenageShoes.as_view(), name='teenage_shoes'),
    path('status_order/', views.CreateOrderView.as_view(), name='status_order'),
    ]
