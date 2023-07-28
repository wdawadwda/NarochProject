from django.urls import path
from . import views
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

urlpatterns = [
    path('', user_passes_test(is_admin)(views.admin_for_staff), name="admin_for_staff"),
    path('comment_moderation/', user_passes_test(is_admin)(views.comment_moderation), name="comment_moderation"),
    path('create_comment/', user_passes_test(is_admin)(views.create_comment), name="create_comment"),
    path('comment_moderation/<int:pk>/', user_passes_test(is_admin)(views.comment_detail), name='comment_detail'),
    path('comment_moderation/<int:pk>/update', user_passes_test(is_admin)(views.CommentUpdateView.as_view()), name='comment_update'),
    path('comment_moderation/<int:pk>/delite', user_passes_test(is_admin)(views.CommentDeliteView.as_view()), name='comment_delite'),

    path('gallery_moderation/', user_passes_test(is_admin)(views.gallery_moderation), name="gallery_moderation"),
    path('create_photo/', user_passes_test(is_admin)(views.create_photo), name="create_photo"),
    path('gallery_moderation/<int:pk>/', user_passes_test(is_admin)(views.gallery_detail), name='gallery_detail'),
    path('gallery_moderation/<int:pk>/update', user_passes_test(is_admin)(views.GalleryUpdateView.as_view()), name='photo_update'),
    path('gallery_moderation/<int:pk>/delite', user_passes_test(is_admin)(views.GalleryDeliteView.as_view()), name='photo_delite'),
]
