from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Kategorien, Bilder
from django.views.generic.detail import DetailView
# Create your views here.

class GalleryView(TemplateView):
    template_name = 'gallery_app/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kategorie_gallery = Kategorien.objects.all()
        context['kategorie_gallery'] = kategorie_gallery
        return context


class GalleryDetailView(DetailView):
    model = Bilder
