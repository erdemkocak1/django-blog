from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from uygulama import models
from uygulama.models import Blog, Category


def blog(request):
    blog_list = Blog.objects.filter(durum=True)  # Tüm blog listesi içinde durumu erişime açık olanları filtreler ve onları bir listeye atar.

    # liste=[]
    # for k in range (1,len(blog_list)+1):
    #     liste.append(k)

    # list1=[]
    # for c in blog_list:
    #     list1.append(c.category)
    # # print(list1)
    #
    # list2 = []
    # for k in list1:
    #     if k not in list2:
    #         list2.append(k)
    # list2.__str__().replace("<Category:", "")
    # print(list2)

    list3 = []
    for s in blog_list:
        list3.append(s.category.slug)

    list4 = []
    for l in list3:
        if l not in list4:
            list4.append(l)

    list5 = []
    for m in blog_list:
        list5.append(m.title)

    list6 = []
    list6.extend(list5[-10:])
    list6 = list6[::-1]

    page = request.GET.get('sayfa', 1)

    paginator = Paginator(blog_list, 20)
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)

    return render(request, 'main.html', {'blog_list': blog_list, 'list4': list4, 'list6': list6})  # Yukarıdaki filtre uygulandıktan sonra listelenen içeriği belirtilen html sayfasına yazdırma işlemini yapar.


def blogdetay(request, slug):
    blog_detay = Blog.objects.get(slug=slug)

    return render(request, 'blog_detay.html', {'blog_detay': blog_detay})


def categorysec(request, slug):
    category_sec = Blog.objects.filter(category__slug=slug)

    page = request.GET.get('sayfa', 1)

    paginator = Paginator(category_sec, 20)
    try:
        category_sec = paginator.page(page)
    except PageNotAnInteger:
        category_sec = paginator.page(1)
    except EmptyPage:
        category_sec = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category_sec': category_sec})
