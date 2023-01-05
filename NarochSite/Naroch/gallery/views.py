from django.shortcuts import render
from .models import Photo
from django.core.paginator import Paginator

def photo_galery(request):
    photo = Photo.objects.all().order_by('id')
    paginator = Paginator(photo, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/photo_galery.html', {'page_obj': page_obj})

def photo_outside(request):
    photo = Photo.objects.filter(category='улица')
    paginator = Paginator(photo, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/photo_outside.html', {'page_obj': page_obj})

def photo_area(request):
    photo = Photo.objects.filter(category='участок')
    paginator = Paginator(photo, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/photo_area.html', {'page_obj': page_obj})

def photo_first_house(request):
    photo = Photo.objects.filter(category='первый_дом')
    paginator = Paginator(photo, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/photo_first_house.html', {'page_obj': page_obj})

def photo_second_house(request):
    photo = Photo.objects.filter(category='второй_дом')
    paginator = Paginator(photo, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/photo_second_house.html', {'page_obj': page_obj})

def photo_bath_house(request):
    photo = Photo.objects.filter(category='баня')
    paginator = Paginator(photo, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/photo_bath_house.html', {'page_obj': page_obj})