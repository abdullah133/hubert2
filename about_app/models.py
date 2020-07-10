from django.db import models
from django.urls import reverse




class AboutModel(models.Model):
    name = models.CharField('Name',max_length=300)
    aufgaben = models.CharField('Aufgaben',max_length=300, blank=True)
    beschreibung = models.TextField('Obere Beschreibung',default='text')


    class Meta:
        verbose_name_plural = " Die erste Beschreibung"
        verbose_name = " erste Beschreibung"
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('about_app:about_page')




class UeberMichBeschreibungen(models.Model):
    titel = models.CharField("Überschrift",max_length=300)
    beschreibung = models.TextField("Untere Beschreibung",blank=True, null=True)

    class Meta:
        verbose_name_plural = "Die zweite Beschreibung"
        verbose_name = "zweite Beschreibung"


    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse('about_app:about_page')
