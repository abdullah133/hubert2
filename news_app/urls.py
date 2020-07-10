from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'news_app'





urlpatterns = [

    path('News/', PostListView.as_view(), name='news_list_page'),
    path('news_detail/<int:pk>/', PostDetailView.as_view(), name='news_detail_page'),


]
