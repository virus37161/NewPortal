from django.urls import path
# Импортируем созданное нами представление
from .views import ListNews,DetailNew,ListNewss,CreateNews, CreateArticle, NewsUpdate,ArticlesUpdate, DeleteNews,DeleteArticle


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('news/', ListNews.as_view(), name = 'all_news'),
   path('news/<int:pk>',DetailNew.as_view(), name="news"),
   path('news/search',ListNewss.as_view()),
   path('news/create/', CreateNews.as_view()),
path('articles/create/', CreateArticle.as_view()),
path('news/<int:pk>/edit/', NewsUpdate.as_view()),
path('articles/<int:pk>/edit/', ArticlesUpdate.as_view()),
path('articles/<int:pk>/delete/', DeleteArticle.as_view()),
path('news/<int:pk>/delete/', DeleteNews.as_view()),
]