from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from uygulama.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'timeread', 'dateet', 'durum')  #

    fields = ('title', 'slug', 'category', 'body', 'author', 'durum', 'timeread')

    list_filter = ('author', 'category', 'dateet')
    list_display_links = ('title', 'category')
    ordering = ('author', 'title', 'dateet')
    view_on_site = True
    search_fields = ['title', 'author']
    list_max_show_all = False
    list_per_page = 5
    prepopulated_fields = {"slug": ("category", "title")}


admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'adet', 'durum')
    fields = ('title', 'durum')


admin.site.register(Category, CategoryAdmin)
