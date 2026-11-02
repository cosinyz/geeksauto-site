from django.contrib import admin
from .models import Car, Contact, Feature, Settings, Slide


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'year', 'position')
    list_filter = ('category', 'year')
    search_fields = ('name', 'engine', 'gearbox')
    ordering = ('position', 'id')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    search_fields = ('title', 'description')
    ordering = ('position', 'id')


admin.site.register(Settings)
admin.site.register(Slide)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'car')
    search_fields = ('name', 'phone', 'car')