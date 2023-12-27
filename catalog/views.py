from django.shortcuts import render

from catalog.models import Category, Product


def contacts(requests):
    return render(requests, 'catalog/contacts.html')


def products(requests):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Наш ассортимент'
    }
    return render(requests, 'catalog/products.html', context)


def home(requests):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Все категории техники'
    }
    return render(requests, 'catalog/home.html', context)


def category_products(requests, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Все наши {category_item.category_name}'
    }
    return render(requests, 'catalog/category_products.html', context)
