from django.shortcuts import render
from .models import Car, Feature, Settings, Slide


def index(request):
    settings = Settings.objects.first()
    slide = Slide.objects.first()
    cars = Car.objects.all()
    features = Feature.objects.all()
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