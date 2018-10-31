from django.contrib import admin

# Register your models here.
from django.contrib import admin

from uygulama.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'timeread','dateet' ,'durum')

    fields = ('title', 'slug', 'category', 'body', 'author','durum', 'timeread')

    list_filter = ('title', 'category')
    list_display_links = ('title','category')
    ordering = ('author', 'title')
    view_on_site = True
    search_fields = ['title', 'author']
    # list_max_show_all = 10
    list_per_page = 5




admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'durum')
    fields = ('title', 'durum')

admin.site.register(Category, CategoryAdmin)
