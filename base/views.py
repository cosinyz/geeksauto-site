import re

from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Contact, Car, Feature, Settings, Slide


def index(request):
    settings = Settings.objects.first()
    slide = Slide.objects.first()
    cars = Car.objects.all()
    features = Feature.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        car = request.POST.get('car', '').strip()

        if not name or len(re.sub(r'\D', '', phone)) < 10:
            messages.error(request, 'Укажите имя и корректный номер телефона.')
        elif car and not Car.objects.filter(name=car).exists():
            messages.error(request, 'Выберите автомобиль из каталога.')
        else:
            Contact.objects.create(name=name, phone=phone, car=car)
            messages.success(
                request,
                f'Спасибо, {name}! Мы перезвоним вам в ближайшее время.',
            )
        return redirect('index-page')

    return render(
        request,
        'index.html',
        {
            'settings': settings,
            'slide': slide,
            'cars': cars,
            'features': features,
        },
    )