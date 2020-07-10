from django.db import models
from stdimage import StdImageField
from django.urls import reverse
# # Create your models here.
# class Kategorien(object):
#     """docstring for ."""
#
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg
#
# class Bilder(object):
#     """docstring for ."""
#     kategorie = models.ForeignKey(Kategorien, on_delete=models.CASCADE)
#
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg



class Kategorien(models.Model):
    kategorie_name = models.CharField(max_length=30,blank=True, null=True,)

    def __str__(self):
        return "%s" % (self.kategorie_name)

    class Meta:
        verbose_name_plural = " Kategorien"
        verbose_name = "Kategorie"
# liste = (
#
# ('weiss':'weiss'),
# ('schwarz':'schwarz')
# )

class Bilder(models.Model):
    titel = models.CharField(max_length=30,blank=True, null=True,)
    text_1 = models.TextField('Text 1',blank=True, null=True)
    text_2 = models.TextField('Text 2',blank=True, null=True)
    kategorie = models.ForeignKey(Kategorien, on_delete=models.CASCADE)
    bild = StdImageField("Bild",upload_to='News/bilder/', blank=True, null=True, variations={'large': (1200, 600),'middle': (600, 300)})
    datum = models.DateTimeField("Post-Datum",blank=True, null=True)

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name_plural = " Bilder"
        verbose_name = "Bild"

    def get_absolute_url(self):
        return reverse('gallery_app:gallery_detail_page', kwargs={'pk': self.pk})
