from django.contrib.sitemaps import Sitemap
from about_app.models import AboutModel, UeberMichBeschreibungen
from django.urls import reverse
from contact_app.models import KontaktInfo
from news_app.models import NewsModel
from base_app.models import HomeSlider, HomeBeschreibung
from gallery_app.models import Kategorien, Bilder

class AboutModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return AboutModel.objects.all()

class UeberMichBeschreibungenSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return UeberMichBeschreibungen.objects.all()

class HomeBeschreibungSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return HomeBeschreibung.objects.all()


class HomeSliderSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return HomeSlider.objects.all()



class NewsSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return NewsModel.objects.all()




class KontaktInfoSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return KontaktInfo.objects.all()
