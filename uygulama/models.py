from django.db import models


# Create your models here.
#


#
class Category(models.Model):
    title = models.CharField('Kategori', max_length=100, unique=True, help_text="Kategori İsmi Yazılacak")
    durum = models.BooleanField('Erişime Açık', default=True)


class Blog(models.Model):
    onemin = '1'
    twomin = '2'
    threemin = '3'
    fourmin = '4'
    CHOICES = ((onemin, '1dk'), (twomin, '2dk'), (threemin, '3dk'), (fourmin, '4dk'),)

    title = models.CharField('Başlık', max_length=100, unique=True, blank=False, null=False, default='', help_text="Başlık buraya yazılacak")
    slug = models.SlugField(max_length=100, unique=True, null=True)
    body = models.TextField('İçerik', help_text="Makale buraya yazılacak", blank=False, null=False, default='')
    author = models.CharField('Yazar', max_length=20, help_text="Yazar", null=False, default='')
    category = models.CharField('Kategori', max_length=10, blank=False, null=False, default='')
    durum = models.BooleanField('Erişim', default=True)
    dateet = models.DateTimeField(auto_now=True)
    timeread = models.CharField('Okuma Süresi', max_length=2, choices=CHOICES, default=2)
