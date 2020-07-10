from django.db import models
from stdimage import StdImageField
from django.urls import reverse
# Create your models here.
class HomeBeschreibung(models.Model):
    titel = models.CharField('Titel',max_length=255)
    untertitel = models.TextField('Untertitel',blank=True, null=True)


    class Meta:
        ordering = ['id']
        verbose_name_plural = "Slider"
        verbose_name = "Slider"

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse('base_app:home_page')


class HomeSlider(models.Model):
    titel = models.CharField('Titel',max_length=255)
    text = models.TextField('Text',)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Start Seite Beschreibung"
        verbose_name = "Start Seite Beschreibung"

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse('base_app:home_page')
