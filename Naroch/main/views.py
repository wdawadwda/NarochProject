from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import JsonResponse

def index(request):
    return render(request, 'main/index.html')


def calendar(request):
    return render(request, 'main/calendar.html')

# Форма отправки данных
#______________________________________________________________

def booking(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Данные для связи'
            
            body = {
                '1': "Имя: ", 'name': form.cleaned_data['name'], '5': " ",
                '2': "Email: ", 'email': form.cleaned_data['email'], '6': " ",
                '3': "Мессенджеры: ", 'messengers': form.cleaned_data['messengers'], '7': " ",
                '4': "Телефон: ", 'phone': form.cleaned_data['phone'], '8': " ",
            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message,
                    'naroch17guesthouse@gmail.com',
                    ['wdawadwda1235712357@gmail.com'])
                return JsonResponse({'success': True})
            except BadHeaderError:
                return JsonResponse({'error': 'Ошибка отправки'})

        return JsonResponse({'error': form.errors})
    else:
        form = ContactForm()
    return render(request, 'main/booking.html', {'form': form})
