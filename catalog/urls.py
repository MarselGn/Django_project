from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, contacts, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, \
    BlogDeleteView
from catalog.views import ProductListView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>', CategoryListView.as_view(), name='category_products'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
