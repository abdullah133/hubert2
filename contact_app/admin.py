from django.contrib import admin
from .models import *





@admin.register(KontaktInfo)
class KontaktInfoAdmin(admin.ModelAdmin):
    list_display = ['name','email']
