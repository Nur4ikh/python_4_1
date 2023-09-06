from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
def cars_view(request):
    cars = models.Cars.objects.all()
    return render(request, 'cars/cars.html', {'cars': cars})

def car_detail_view(request, id):
    cars_id = get_object_or_404(models.Cars, id=id)
    return render(request, 'cars/car_detail.html', {'car_id': cars_id})