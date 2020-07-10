from django.db import models
from django.urls import reverse


class KontaktInfo(models.Model):
    name = models.CharField('Name',max_length=300, default="Hubert Mayr")
    telefon = models.CharField('Telefon Nr.',max_length=300, blank=True, null=True)
    email = models.CharField('E-Mail Adresse',max_length=300)
    facebook_link = models.CharField('Facebook Link',max_length=300, blank=True, null=True)
    beschreibung = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['id']
        verbose_name_plural = " Kontaktinfos"
        verbose_name = "Kontaktinfo"

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('contact_app:contact_page')
