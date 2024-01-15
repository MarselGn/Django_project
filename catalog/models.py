from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_content = models.TextField(verbose_name='описание')
    product_image = models.ImageField(upload_to='catalog/', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price_for_one = models.IntegerField(verbose_name='цена')
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name} {self.price_for_one}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


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
