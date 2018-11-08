
from django.contrib import admin
from django.urls import path

from uygulama import views

urlpatterns = [

    path('cat/<slug:slug>/', views.categorysec),        # cat/ şeklinde gelirse view.py dosyasındaki categorysec kısmı çalışacak ve categorysec kısmı category.html yardımıyla sonuçları sayfaya yazacak.

    path('', views.blog),                          # blog/ şeklinde bir arama gelirse view.py dosyasındaki blog kısmı çalışacak blog kısmı ulaştığı sonuçları main.html yardımıyla sayfaya yazacak.
    path('blog/detay/<slug:slug>/', views.blogdetay),   # blog/detay gibi bir arama gelirse veya makalelerin içeriğine girilmek istenirse burası view.py dosyasındaki blogdetay kısmını çalıştıracak ve sonuçları blog_deay.html yardımıyla sayfaya yazacak.



    path('admin/', admin.site.urls),


]

admin.site.site_header = 'urls.py__admin.site.site_header'
admin.site.site_title = 'urls.py__admin.site.site_title'
admin.site.index_title = 'urls.py__admin.site.index_title'