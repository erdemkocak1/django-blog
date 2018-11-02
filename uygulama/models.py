from django.db import models


class Category(models.Model):
    title = models.CharField('Kategori', max_length=100, unique=True, help_text="Kategori İsmi Yazılacak")
    durum = models.BooleanField('Erişime Açık', default=True)
    adet = models.IntegerField('İçerik Sayısı', default=0)

    slug = models.CharField(('Link'), max_length=100, help_text="Otomatik oluşturulacak", default='')

    def __str__(self):
        return '%s' % self.title


class Meta:
    verbose_name_plural = ('Category')
    verbose_name = ('Category')


class Blog(models.Model):
    CHOICES = (('1', '1dk'), ('2', '2dk'), ('3', '3dk'), ('4', '4dk'), ('5', '5dk'), ('6', '6dk'), ('7', '7dk'),)

    title = models.CharField('Başlık', max_length=100, unique=True, blank=False, null=False, default='', help_text="Başlık buraya yazılacak")
    slug = models.CharField(('Link'), max_length=100, help_text="Otomatik oluşturulacak", default='')
    body = models.TextField('İçerik', help_text="Makale buraya yazılacak", blank=False, null=False, default='')
    author = models.CharField('Yazar', max_length=20, help_text="Yazar", null=False, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategori')
    durum = models.BooleanField('Erişim', default=True)
    dateet = models.DateTimeField('Oluşturulma Zamanı', auto_now=True)
    timeread = models.CharField('Okuma Süresi', max_length=2, choices=CHOICES, default=1)

    class Meta:
        verbose_name_plural = ('Blog')
        verbose_name = ('Blog')
