from django.db import models

# Create your models here.
#


#
class Category(models.Model):
    # title = models.CharField(_('Başlık'), max_length=100, unique=True, help_text=_(u"Başlık Buraya"))
    title = models.CharField(max_length=100, unique=True, help_text="Başlık buraya yazılacak")

#     slug = models.SlugField(max_length=100, db_index=True)
#     durum           = models.BooleanField(_('Durum'), default=True)
#
    # def __str__(self):
    #     return '%s' %  self.title
    #
    # class Meta:
    #     verbose_name_plural         =           ('Categorys')
    #     verbose_name                =           ('Category')

class Blog (models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=('Kategori'))

