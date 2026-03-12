from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('product/<slug:slug>/', product, name='product'),
    
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    
    path('cart/', cart, name='cart'),
    path('profile/', profile, name='profile'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
    path('order-details/', order_details, name='order_details'),
    path('addresses/', addresses, name='addresses'),
    path('wishlist/', wishlist, name='wishlist'),
    
    path('admin/', admin_dashboard, name='admin_dashboard'),
    
    path('admin/categories/', admin_categories, name='admin_categories'),
    path('admin/categories/create/', admin_category_create, name='admin_category_create'),
    path('admin/categories/<int:id>/edit/', admin_category_edit, name='admin_category_edit'),
    path('admin/categories/<int:id>/delete/', admin_category_delete, name='admin_category_delete'),
    
    path('admin/products/', admin_products, name='admin_products'),
    path('admin/products/create/', admin_product_create, name='admin_product_create'),
    path('admin/products/<int:id>/edit/', admin_product_edit, name='admin_product_edit'),
    path('admin/products/<int:id>/delete/', admin_product_delete, name='admin_product_delete'),
    
    path('admin/colors/', admin_colors, name='admin_colors'),
    path('admin/colors/create/', admin_color_create, name='admin_color_create'),
    path('admin/colors/<int:id>/edit/', admin_color_edit, name='admin_color_edit'),
    path('admin/colors/<int:id>/delete/', admin_color_delete, name='admin_color_delete'),
    
    path('admin/sizes/', admin_sizes, name='admin_sizes'),
    path('admin/sizes/create/', admin_size_create, name='admin_size_create'),
    path('admin/sizes/<int:id>/edit/', admin_size_edit, name='admin_size_edit'),
    path('admin/sizes/<int:id>/delete/', admin_size_delete, name='admin_size_delete'),
    
    path('admin/products/<int:product_id>/variants/create/', admin_variant_create, name='admin_variant_create'),
    path('admin/variants/<int:id>/edit/', admin_variant_edit, name='admin_variant_edit'),
    path('admin/variants/<int:id>/delete/', admin_variant_delete, name='admin_variant_delete'),
    path('admin/variants/images/<int:id>/delete/', admin_variant_image_delete, name='admin_variant_image_delete'),
]
