from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название сайта')
    logo = models.ImageField(upload_to='logo/', verbose_name='Логотип')
    description = models.TextField(verbose_name='Описание сайта')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'


class Slide(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок слайда')
    image = models.ImageField(upload_to='slider/', verbose_name='Изображение слайда')
    description = models.TextField(verbose_name='Описание слайда')
    sales = models.CharField(max_length=255, default=False, verbose_name='Машин продано')
    age = models.CharField(max_length=255, verbose_name='Лет на рынке')
    clients = models.IntegerField(verbose_name='Довольных клиентов')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '2) Слайд'
        verbose_name_plural = '2) Слайды'


class Car(models.Model):
    class Category(models.TextChoices):
        SEDAN = 'sedan', 'Седан'
        SUV = 'suv', 'Кроссовер'
        SPORT = 'sport', 'Спорт'

    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        verbose_name='Категория',
    )
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    year = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    engine = models.CharField(max_length=255, verbose_name='Двигатель')
    gearbox = models.CharField(max_length=100, verbose_name='Коробка передач')
    image = models.ImageField(
        upload_to='cars/',
        blank=True,
        verbose_name='Фото',
    )
    image_url = models.URLField(blank=True, verbose_name='Ссылка на фото')
    position = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('position', 'id')
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Feature(models.Model):
    icon = models.CharField(max_length=20, verbose_name='Иконка')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    position = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('position', 'id')
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'