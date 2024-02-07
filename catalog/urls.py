from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeView, contacts, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, \
    BlogDeleteView, ProductDetailView
from catalog.views import ProductListView, CategoryListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', (HomeView.as_view()), name='index'),
    path('categories/', CategoryListView.as_view(), name='category'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/catalog/', ProductListView.as_view(), name='category_products'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('<int:pk>/catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/create/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/product/', cache_page(60)(ProductDetailView.as_view()), name='product'),
]
