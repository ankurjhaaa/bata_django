from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView,
    ProductVariantListCreateView, ProductVariantDetailView
)

urlpatterns = [
    # Category API URLs
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Product API URLs
    path('api/products/', ProductListCreateView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Product Variant API URLs
    path('api/variants/', ProductVariantListCreateView.as_view(), name='variant-list'),
    path('api/variants/<int:pk>/', ProductVariantDetailView.as_view(), name='variant-detail'),
]
