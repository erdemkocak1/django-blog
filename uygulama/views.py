from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from uygulama import models
from uygulama.models import Blog, Category


def blog(request):
    blog_list = Blog.objects.filter(durum=True)

    return render(request, 'main.html', {'blog_list': blog_list})


def blogdetay(request, slug):
    blog_detay = Blog.objects.get(slug=slug)

    return render(request, 'blog_detay.html', {'blog_detay': blog_detay})

#
# def categorysec(request, category):
#     category_sec = Blog.objects.filter(category=category)
#
#     return render(request, 'category.html', {'category_sec': category_sec})
