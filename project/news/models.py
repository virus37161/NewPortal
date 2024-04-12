from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
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

class Category(models.Model):
    name_category = models.TextField(unique= True)

class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete = models.CASCADE)
    Char = models.CharField(max_length = 2, choices = Post_news)
    some_data = models.DateField (auto_now_add = True)
    some_time = models.TimeField (auto_now_add = True)
    name = models.TextField()
    text = models.TextField()
    rate = models.IntegerField(default = 0)
    post_category = models.ManyToManyField(Category, through = 'PostCategory')

    def preview(self):
        return self.text[0:128]+"..."

    def like(self):
        self.rate +=1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

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

