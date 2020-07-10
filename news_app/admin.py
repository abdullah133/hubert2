
from .models import *
from django.contrib import admin

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['titel','image_tag','pdf_tag']
