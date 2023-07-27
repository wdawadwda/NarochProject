from distutils.log import error
from email import message
import email
from urllib import request
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, ReviewsForm, UserPasswordChangeForm, EmailChangeForm
from django.contrib import messages
from .models import Reviews
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Отзывы
#______________________________________________________________
def reviews(request):
    reviews = Reviews.objects.filter(category='верифицирован').order_by('-reviews_date')
    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            try:
                new_post = form.save(commit=False) # Для автоподставки юзера
                new_post.username = request.user # Для автоподставки юзера
                form.save()
                messages.success(request, "Спасибо за ваш комментарий")
                return redirect("reviews")
            except ValueError:
                messages.error(request,'Зарегистрируйтесь, чтобы оставить комментарий')
        else:
            messages.error(request,'Что-то пошло не так')

    form = ReviewsForm()
    data = {
        'form' : form,
        'error' : error,
        'reviews' : reviews
    }
    return render(request, 'user/reviews.html', {'form' : form,'error' : error,'reviews' : reviews, 'page_obj': page_obj})
#______________________________________________________________

# Регистрация
#______________________________________________________________
def register(request): # Отправка письма с подтверждением
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.is_active = False
           user.save()
           current_site = get_current_site(request)
           mail_subject = 'Письмо с активацией отправлено на ваш email'
           message = render_to_string('user/message_templates/msg_active_email.html',{
            'user': user, 
            'domain': current_site.domain, 
            'uid':urlsafe_base64_encode(force_bytes(user.pk)), 
            'token':account_activation_token.make_token(user)
           })
           to_email = form.cleaned_data.get('email')
           email = EmailMessage(
            mail_subject, message, to=[to_email]
           )
           email.send()
           messages.success(request, "Письмо с активацией отправлено на ваш email")
        else:
            messages.error(request,"Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {"form": form})

# Подтверждение регистрации
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'user/user_congrat_reg.html')
    else: 
        return HttpResponse('Ссылка активации недействительна')
#______________________________________________________________

# login/logout
#______________________________________________________________
def user_login(request):
    if request.method == 'POST':    
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('reviews')
    else:
        form = UserLoginForm()
    return render(request, 'user/user_login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('user_login')
#______________________________________________________________

# Изменить пароль/email
#______________________________________________________________
@login_required
def user_change_password(request):
    if request.method == 'POST':    
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль был успешно изменён")
        else:
            messages.error(request,"Что-то пошло не так")
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'user/user_change_password.html', {"form": form})


def password_change_done(request):
    logout(request)
    return redirect ('user_login')

@login_required
def user_change_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['email1']  == form.cleaned_data['email2'] and form.cleaned_data['email']  != form.cleaned_data['email1']:
                request.user.email = form.cleaned_data['email1']
                request.user.save()
                messages.success(request, "Email был успешно изменён")
            elif form.cleaned_data['email']  != form.cleaned_data['email1']:
                messages.error(request, "Новый email должен отличаться от старого")
        else:
            messages.error(request, "Ошибка смены email")
    else:
        form = EmailChangeForm()
    return render(request, 'user/user_change_email.html', {"form": form})
