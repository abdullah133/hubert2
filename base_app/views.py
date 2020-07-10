from django.shortcuts import render

from django.views.generic import ListView
from .models import HomeBeschreibung, HomeSlider



class HomeView(ListView):
    model = HomeSlider
    template_name = 'base_app/home.html'


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['home_beschreibung'] = HomeBeschreibung.objects.all()
        return context
