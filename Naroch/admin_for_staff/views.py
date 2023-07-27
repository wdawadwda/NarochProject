from django.shortcuts import render, redirect
from user.models import Reviews
from gallery.models import Photo
from .forms import ReviewsAdminFrom, PhotoAdminFrom
from django.contrib import messages

from django.views.generic import DetailView, UpdateView, DeleteView

def admin_for_staff(request):
    return render(request, 'admin_for_staff/admin_for_staff.html')

#! Комментарии
#! ______________________________________________________________

def comment_moderation(request):
    comments_all = Reviews.objects.order_by('-category')
    context = {
        'comments_all' : comments_all,
    }

    return render(request, 'admin_for_staff/comment_moderation.html', context)

def create_comment(request):
    if request.method == 'POST':
        form = ReviewsAdminFrom(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False) # Для автоподставки юзера
            new_post.username = request.user
            form.save()
            return redirect('comment_moderation')
        else:
            messages.error(request,'Ошибка отправки')

    form = ReviewsAdminFrom()
    data = {
        'form' : form,
    }
    return render(request, 'admin_for_staff/create_comment.html', data)
    
def comment_detail(request, pk):
    comment = Reviews.objects.get(pk=pk)
    context = {
        'comment': comment,
    }
    return render(request, 'admin_for_staff/comment_detail.html', context)

class CommentUpdateView(UpdateView):
    model = Reviews
    template_name = 'admin_for_staff/create_comment.html'
    context = 'comment'
    form_class = ReviewsAdminFrom

class CommentDeliteView(DeleteView):
    model = Reviews
    template_name = 'admin_for_staff/delite_comment.html'
    context = 'comment'
    success_url = '/admin_for_staff/comment_moderation/'

#! Галерея
#! ______________________________________________________________
def gallery_moderation(request):
    gallery_all = Photo.objects.order_by('-id')
    context = {
        'gallery_all' : gallery_all,
    }

    return render(request, 'admin_for_staff/gallery_moderation.html', context)

def create_photo(request):
    if request.method == 'POST':
        form = PhotoAdminFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_moderation')
        else:
            messages.error(request,'Ошибка отправки')

    form = PhotoAdminFrom()
    data = {
        'form' : form,
    }
    return render(request, 'admin_for_staff/create_photo.html', data)

def gallery_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        'comment': photo,
    }
    return render(request, 'admin_for_staff/gallery_detail.html', context)

class GalleryUpdateView(UpdateView):
    model = Photo
    template_name = 'admin_for_staff/create_photo.html'
    context = 'photo'
    form_class = PhotoAdminFrom

class GalleryDeliteView(DeleteView):
    model = Photo
    template_name = 'admin_for_staff/photo_delite.html'
    context = 'comment'
    success_url = '/admin_for_staff/gallery_moderation/'
    