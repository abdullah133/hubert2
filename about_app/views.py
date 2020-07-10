from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import AboutModel, UeberMichBeschreibungen


class AboutView(TemplateView):
    template_name = 'about_app/about.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        haupt_beschreibung = AboutModel.objects.all()
        context['haupt_beschreibung'] = haupt_beschreibung
        untere_zusetzliche_beschreibung = UeberMichBeschreibungen.objects.all()
        context['untere_zusetzliche_beschreibung'] = untere_zusetzliche_beschreibung
        return context
