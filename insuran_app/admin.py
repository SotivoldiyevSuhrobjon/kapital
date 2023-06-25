from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Sugurta)
class SugurtaAdmin(TranslationAdmin):
    list_display = ['title', 'description']


@admin.register(Support)
class SupportaAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'phone']


@admin.register(Social)
class Social(admin.ModelAdmin):
    list_display = ['instagram', 'facebook', 'youtube', 'telegram']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name','region']

admin.site.register(Region)
admin.site.register(Sport)

@admin.register(RelatedSport)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name','sport']

