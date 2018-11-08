from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from uygulama.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'timeread', 'dateet', 'durum')   # Admin blog sayfasında içerik listelenirken içerikle ilgili gösterilecek nitelikler.

    fields = ('title', 'slug', 'category', 'body', 'author', 'durum', 'timeread')   # Yeni makale kaydı yapılacağı zaman doldurulacak alanlar.

    list_filter = ('author', 'category', 'dateet', 'durum')                                  # Admin sayfasında listelenen içerik için filtre uygulanacak nitelikler.(Bu durumda yazar-kategori-zaman gibi niteliklere göre filtre uygulanacak )
    list_display_links = ('title', 'category')                                      # Tıklandığında başka bir sayfaya yönlendirecek nitelikler için kullanılır.
    ordering = ('author', 'title', 'dateet')
    view_on_site = True
    search_fields = ['title', 'author']                                             # Arama yapıldığı zaman aramanın sorgulayacağı alanları belirtir
    list_max_show_all = False                                                       # Sayfada bütün içeriğin gösterilmesini ve belirlenen sayının üzerine çıkılmasını engeller.
    list_per_page = 5                                                               # Admin sayfasında tek sayfada gösterilecek içeriğin sayısını belirtir.
    prepopulated_fields = {"slug": ("category", "title")}


admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'adet', 'durum', 'slug')                               # Admin kategori sayfasında kategoriler için gösterilecek nitelikler
    fields = ('title', 'durum', 'slug')                                             # Yeni kategori oluşturulacağı zaman doldurulacak alanlar.
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
