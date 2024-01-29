from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_content = models.TextField(verbose_name='описание')
    product_image = models.ImageField(upload_to='catalog/', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price_for_one = models.IntegerField(verbose_name='цена', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, **NULLABLE)
    date_last_change = models.DateTimeField(auto_now=True, **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.product_name} {self.price_for_one}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            ('set_is_published', 'Может публиковать товары'),
            ('set_product_content', 'Может менять описание'),
            ('set_category', 'Может менять категорию'),
        ]


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_content = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    body = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True)
    count_views = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=100, verbose_name='slug')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    number_version = models.IntegerField(**NULLABLE, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='наименование')
    is_activated = models.BooleanField(default=True, verbose_name='активна')

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
