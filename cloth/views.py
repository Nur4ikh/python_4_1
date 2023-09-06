from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import generic
from . import models, forms
from cloth.models import StatusOrder


class ProductView(ListView):
    template_name = 'cloth/product.html'
    queryset = models.Product.objects.filter().order_by('-id')

    def get_tag(self, obj):
        return obj.tag.name_tag

    def get_queryset(self):
        # return models.Product.objects.all()
        return models.Product.objects.filter().order_by('-id')


'''по тэгам'''


class MenShoes(ListView):
    template_name = 'cloth/men_shoes.html'
    queryset = models.Product.objects.filter(tag__name_tag='мужские')

    def get_queryset(self):
        return models.Product.objects.filter(tag__name_tag='мужские')


class WomenShoes(ListView):
    template_name = 'cloth/women_shoes.html'
    queryset = models.Product.objects.filter(tag__name_tag='женские')

    def get_queryset(self):
        return models.Product.objects.filter(tag__name_tag='женские')


class KidsShoes(ListView):
    template_name = 'cloth/kids_shoes.html'
    queryset = models.Product.objects.filter(tag__name_tag='детские')

    def get_queryset(self):
        return models.Product.objects.filter(tag__name_tag='детские')


class TeenageShoes(ListView):
    template_name = 'cloth/teenage_shoes.html'
    queryset = models.Product.objects.filter(tag__name_tag='подростковые')

    def get_queryset(self):
        return models.Product.objects.filter(tag__name_tag='подростковые')


'''Статус заказа'''

class CreateOrderView(generic.CreateView):
    template_name = 'cloth/status_order.html'
    form_class = forms.StatusOrderForm
    queryset = StatusOrder.objects.all()
    success_url = '/product/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)
