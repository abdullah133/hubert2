from django.contrib import admin
from .models import *



@admin.register(Kategorien)
class KategorienAdmin(admin.ModelAdmin):
    list_display = ['kategorie_name',]



@admin.register(Bilder)
class BilderAdmin(admin.ModelAdmin):
    list_display = ['kategorie','bild']
