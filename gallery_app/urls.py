from django.urls import path

from .views import GalleryView,GalleryDetailView

app_name = 'gallery_app'





urlpatterns = [

    path('Ausstellungen/', GalleryView.as_view(), name='gallery_page'),
    path('Ausstellungen/<int:pk>/', GalleryDetailView.as_view(), name='gallery_detail_page'),

]
