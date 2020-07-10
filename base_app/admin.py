from django.contrib import admin
from .models import *



@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['titel','text']



@admin.register(HomeBeschreibung)
class HomeBeschreibungAdmin(admin.ModelAdmin):
    list_display = ['titel','untertitel']
