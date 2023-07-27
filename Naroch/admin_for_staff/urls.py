from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_for_staff, name="admin_for_staff"),
    path('comment_moderation/', views.comment_moderation, name="comment_moderation"),
    path('create_comment/', views.create_comment, name="create_comment"),
    path('comment_moderation/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('comment_moderation/<int:pk>/update', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment_moderation/<int:pk>/delite', views.CommentDeliteView.as_view(), name='comment_delite'),

    path('gallery_moderation/', views.gallery_moderation, name="gallery_moderation"),
    path('create_photo/', views.create_photo, name="create_photo"),
    path('gallery_moderation/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('gallery_moderation/<int:pk>/update', views.GalleryUpdateView.as_view(), name='photo_update'),
    path('gallery_moderation/<int:pk>/delite', views.GalleryDeliteView.as_view(), name='photo_delite'),
]
