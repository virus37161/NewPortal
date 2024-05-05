from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView,TemplateView
from .models import *
from .filters import NewsFilter
from .forms import NewsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

import datetime

class ListNews(ListView):
    model = Post
    ordering = '-some_data'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context



class DetailNew(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

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



class CreateNews(PermissionRequiredMixin,CreateView):
    permission_required = ('news.add_post')
    form_class= NewsForm
    model = Post
    template_name = "news_create.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.Char = 'NW'
        post.post_author = Author.objects.get(user_id = self.request.user.id)
        Author_id = Author.objects.get(user_id=self.request.user.id).id
        if len(Post.objects.filter(post_author_id = Author_id).all().filter(some_data = datetime.datetime.today().strftime('%Y-%m-%d')).all()) <= 2:
            self.object = form.save()
        else:
            return render(self.request, "Many_create.html")
        return super().form_valid(form)

class CreateArticle(PermissionRequiredMixin,CreateView):
    permission_required = ('news.add_post')
    form_class= NewsForm
    model = Post
    template_name = "news_create.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.Char = 'PS'
        post.post_author = Author.objects.get(user_id=self.request.user.id)
        Author_id = Author.objects.get(user_id=self.request.user.id).id
        if len(Post.objects.filter(post_author_id=Author_id).all().filter(
                some_data=datetime.datetime.today().strftime('%Y-%m-%d')).all()) <= 2:
            self.object = form.save()
        else:
            return render(self.request, "Many_create.html")
        return super().form_valid(form)



class NewsUpdate(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    permission_required = ('news.change_post')
    form_class = NewsForm
    model = Post
    template_name = 'news_update.html'

class ArticlesUpdate(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    permission_required = ('news.change_post')
    form_class = NewsForm
    model = Post
    template_name = 'article_update.html'

class DeleteNews(PermissionRequiredMixin,DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('all_news')


class DeleteArticle(PermissionRequiredMixin,DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('all_news')

@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
        Author.objects.create(user_id = request.user.id)
    return redirect('/news')

@login_required
def subscribe (request,pk):
    user = request.user
    category = Category.objects.get(id = pk)
    category.subscribers.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def unsubscribe (request,pk):
    user = request.user
    category = Category.objects.get(id = pk)
    category.subscribers.remove(user)
    return  HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))