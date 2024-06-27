from django.contrib import admin
from .models import Post, Category

from modeltranslation.admin import TranslationAdmin

class PostAdmin (admin.ModelAdmin):
    list_display = ('post_author','name', 'Char', 'text')
    list_display_links = ('name','text')
    search_fields = ('post_author', 'Char')

class CategoryAdmin(TranslationAdmin):
    model = Category

admin.site.register(Post, PostAdmin)
admin.site.register(Category)