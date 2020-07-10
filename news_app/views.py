from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import NewsModel


class PostListView(ListView):
    model = NewsModel
    template_name = 'news_app/news_list.html'
    paginate_by = 2


class PostDetailView(DetailView):

    model = NewsModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
