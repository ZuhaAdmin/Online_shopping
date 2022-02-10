from django.db import models
from django.urls import reverse 
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(verbose_name='Kategoriya_nomi', max_length=20, db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])

class Types(models.Model):
    category = models.ForeignKey(Categories, on_delete=CASCADE)
    name = models.CharField(verbose_name='Turi', max_length=30)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Tur'
        verbose_name_plural = 'Turlar'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_types',
                       args=[self.slug])

class Tags(models.Model):
    name = models.CharField(verbose_name='Tegi', max_length=30)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_tags',
                       args=[self.slug])

class Colors(models.Model):
    name = models.CharField(verbose_name='Rangi', max_length=20)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Rang'
        verbose_name_plural = 'Ranglar'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_colors',
                       args=[self.slug])

class Products(models.Model):
    category = models.ForeignKey(Categories, related_name='products',on_delete=models.CASCADE)
    type = models.ForeignKey(Types, on_delete=CASCADE)
    tag = models.ForeignKey(Tags, on_delete=CASCADE)
    color = models.ForeignKey(Colors, on_delete=CASCADE)
    name = models.CharField(verbose_name='Nomi', max_length=30, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    comment = models.TextField(verbose_name='Izoh', max_length=1500)
    price = models.FloatField(verbose_name='Narxi')
    discount = models.FloatField(verbose_name='Chegirma')
    available = models.BooleanField(default=True)
    position = models.CharField(verbose_name='Holati', max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(verbose_name='Surat', upload_to='products/',
                          blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                      args=[self.id, self.slug])