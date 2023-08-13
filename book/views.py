from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def book_page(request):
    return HttpResponse('hello')

def book_view(request):
    book = models.BookPage.objects.all()
    return render(request, 'book.html', {'book': book})