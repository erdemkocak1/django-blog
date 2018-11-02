"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from uygulama import views

urlpatterns = [


    path('', admin.site.urls),

    path('cat/<slug:slug>/', views.categorysec),        # cat/ şeklinde gelirse view.py dosyasındaki categorysec kısmı çalışacak ve categorysec kısmı category.html yardımıyla sonuçları sayfaya yazacak.

    path('blog/', views.blog),                          # blog/ şeklinde bir arama gelirse view.py dosyasındaki blog kısmı çalışacak blog kısmı ulaştığı sonuçları main.html yardımıyla sayfaya yazacak.
    path('blog/detay/<slug:slug>/', views.blogdetay),   # blog/detay gibi bir arama gelirse veya makalelerin içeriğine girilmek istenirse burası view.py dosyasındaki blogdetay kısmını çalıştıracak ve sonuçları blog_deay.html yardımıyla sayfaya yazacak.



]
