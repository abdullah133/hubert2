from django.contrib import admin
from .models import *


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['name','beschreibung','aufgaben']

@admin.register(UeberMichBeschreibungen)
class UeberMichBeschreibungenAdmin(admin.ModelAdmin):
    list_display = ['beschreibung']
