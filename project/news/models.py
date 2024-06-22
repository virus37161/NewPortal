from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse
from django.core.cache import cache
post = "PS"
New = "NW"
Post_news = [(post,'статья'), (New, "новость")]

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(post_author = self).aggregate(rt = Coalesce(Sum('rate'), 0))['rt']
        comment_rating = Comment.objects.filter(user = self.user).aggregate(rt = Coalesce(Sum('rate'), 0))['rt']
        posts_comment = Comment.objects.filter(post__post_author = self).aggregate(rt = Coalesce(Sum('rate'), 0))['rt']

        self.rating = post_rating * 3 + comment_rating + posts_comment
        self.save()
    def __str__(self):
        return f'{self.user.username.title()}'



class Category(models.Model):
    name_category = models.TextField(unique= True)
    subscribers = models.ManyToManyField(User, related_name = "cotegory_subscribe")

    def __str__(self):
        return f'{self.name_category.title()}'

class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name='Автор')
    Char = models.CharField(max_length = 2, choices = Post_news)
    some_data = models.DateField(auto_now_add = True)
    some_time = models.TimeField (auto_now_add = True)
    name = models.TextField(verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    rate = models.IntegerField(default = 0)
    post_category = models.ManyToManyField(Category, through = 'PostCategory')

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])

    def preview(self):
        return self.text[0:128]+"..."

    def like(self):
        self.rate +=1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'
        ordering = ['-some_data']

class PostCategory(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    some_data = models.DateField(auto_now_add=True)
    some_time = models.TimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()


