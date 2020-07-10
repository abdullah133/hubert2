from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

admin.site.site_header = "Hubertus Admin Page"
admin.site.index_title = "Hubertus Admin Portal"

sitemaps = {'AboutModelSitemap':AboutModelSitemap,
'UeberMichBeschreibungenSitemap':UeberMichBeschreibungenSitemap,
'homebeschreibung':HomeBeschreibungSitemap,
'homeslider':HomeSliderSitemap,
'news':NewsSitemap,
'kontakt':KontaktInfoSitemap,
            }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('base_app.urls')),
    path('', include('about_app.urls')),
    path('', include('gallery_app.urls')),
    path('', include('news_app.urls')),
    path('', include('contact_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
