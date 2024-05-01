from django.urls import path
# Импортируем созданное нами представление
from .views import ListNews,DetailNew,ListNewss,CreateNews, CreateArticle, NewsUpdate,ArticlesUpdate, DeleteNews,DeleteArticle,upgrade_me,subscribe, unsubscribe
from django.contrib.auth.views import LogoutView,TemplateView

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', ListNews.as_view(), name = 'all_news'),
   path('<int:pk>/',DetailNew.as_view(), name="news"),
   path('search/',ListNewss.as_view()),
   path('create/', CreateNews.as_view()),
path('articles/create/', CreateArticle.as_view()),
path('news/<int:pk>/edit/', NewsUpdate.as_view()),
path('articles/<int:pk>/edit/', ArticlesUpdate.as_view()),
path('articles/<int:pk>/delete/', DeleteArticle.as_view(), name = 'delete_article'),
path('news/<int:pk>/delete/', DeleteNews.as_view()),
path('upgrade/', upgrade_me, name = 'upgrade'),
path('logout/', LogoutView.as_view(template_name = 'logout.html'),name='logout'),
path ('logout/confirm/', TemplateView.as_view(template_name = 'logout_confirm.html'), name = 'logout_confirm'),
path('categories/subscribe/<int:pk>/', subscribe, name = 'subscribe'),
path('categories/unsubscribe/<int:pk>/', unsubscribe, name = 'unsubscribe'),
]