from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import *
from .filters import NewsFilter
from .forms import NewsForm
from django.urls import reverse_lazy

class ListNews(ListView):
    model = Post
    ordering = '-some_data'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2




class DetailNew(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class ListNewss(ListView):
    model = Post
    ordering = '-some_data'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class CreateNews(CreateView):
    form_class= NewsForm
    model = Post
    template_name = "news_create.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.Char = 'NW'
        return super().form_valid(form)

class CreateArticle(CreateView):
    form_class= NewsForm
    model = Post
    template_name = "news_create.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.Char = 'PS'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_update.html'

class ArticlesUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_update.html'

class DeleteNews(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('all_news')


class DeleteArticle(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('all_news')