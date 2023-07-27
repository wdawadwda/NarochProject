from django.urls import path
from . import views
from .views import activate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.reviews, name="reviews"),
    path('register', views.register, name="register"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),

    path('password_reset', auth_views.PasswordResetView.as_view(template_name='user/password/password_reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password/password_reset_done.html'), name='password_reset_done'),
    path('rest/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password/password_reset_complete.html'),name='password_reset_complete'),

    path('user_change_password', views.user_change_password, name="user_change_password"),
    path('password/change/', auth_views.PasswordChangeView.as_view(template_name='user/password/password_change.html'), name='password_change'),
    path('password/change/done/', views.password_change_done, name='password_change_done'),
    path('user_change_email', views.user_change_email, name="user_change_email"),
]
