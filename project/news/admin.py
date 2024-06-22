from django.contrib import admin
from .models import Post

class PostAdmin (admin.ModelAdmin):
    list_display = ('post_author','name', 'Char', 'text')
    list_display_links = ('name','text')
    search_fields = ('post_author', 'Char')


admin.site.register(Post, PostAdmin)