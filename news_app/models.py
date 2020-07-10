from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from stdimage import StdImageField
from django.utils.html import format_html
from django.urls import reverse

# Create your models here.
class NewsModel(models.Model):
    titel = models.CharField("Überschrift",max_length=300)
    text = models.TextField("Text",blank=True, null=True)
    bild = StdImageField("Bild",upload_to='News/bilder/', blank=True, variations={'large': (1200, 600),'middle': (600, 300)})
    pdf = models.FileField(upload_to='News/pdf/', blank=True)
    datum = models.DateTimeField("Event-Datum",blank=True, null=True)

    erstellt_am = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"


    def get_absolute_url(self):
        return reverse('news_app:news_detail_page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.titel

    def image_tag(self):
        if self.bild:
            return format_html('<img src="{}" width="320" height="160" />'.format(self.bild.url))
        else:
            return 'Hier ist kein Bild vorhanden'
    def pdf_tag(self):
        if self.pdf:
            return format_html('<a href="{}">{}</a>'.format(self.pdf.url, self.pdf))
        else:
            return 'Hier gibts kein Pdf'


    image_tag.short_description = 'Foto/Bild'
    pdf_tag.short_description = 'Pdf'
