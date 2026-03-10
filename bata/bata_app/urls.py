from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('product/', views.product, name='product'),
    
    # Auth
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    
    # Protected
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('order-details/', views.order_details, name='order_details'),
    path('addresses/', views.addresses, name='addresses'),
    path('wishlist/', views.wishlist, name='wishlist'),
    
    # --- Custom Admin Portal ---
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    
    # Category CRUD
    path('admin/categories/', views.admin_categories, name='admin_categories'),
    path('admin/categories/create/', views.admin_category_create, name='admin_category_create'),
    path('admin/categories/<int:id>/edit/', views.admin_category_edit, name='admin_category_edit'),
    path('admin/categories/<int:id>/delete/', views.admin_category_delete, name='admin_category_delete'),
    
    # Product CRUD
    path('admin/products/', views.admin_products, name='admin_products'),
    path('admin/products/create/', views.admin_product_create, name='admin_product_create'),
    path('admin/products/<int:id>/edit/', views.admin_product_edit, name='admin_product_edit'),
    path('admin/products/<int:id>/delete/', views.admin_product_delete, name='admin_product_delete'),
    
    # Colors CRUD
    path('admin/colors/', views.admin_colors, name='admin_colors'),
    path('admin/colors/create/', views.admin_color_create, name='admin_color_create'),
    path('admin/colors/<int:id>/edit/', views.admin_color_edit, name='admin_color_edit'),
    path('admin/colors/<int:id>/delete/', views.admin_color_delete, name='admin_color_delete'),
    
    # Sizes CRUD
    path('admin/sizes/', views.admin_sizes, name='admin_sizes'),
    path('admin/sizes/create/', views.admin_size_create, name='admin_size_create'),
    path('admin/sizes/<int:id>/edit/', views.admin_size_edit, name='admin_size_edit'),
    path('admin/sizes/<int:id>/delete/', views.admin_size_delete, name='admin_size_delete'),
    
    # Variant CRUD
    path('admin/products/<int:product_id>/variants/create/', views.admin_variant_create, name='admin_variant_create'),
    path('admin/variants/<int:id>/edit/', views.admin_variant_edit, name='admin_variant_edit'),
    path('admin/variants/<int:id>/delete/', views.admin_variant_delete, name='admin_variant_delete'),
    path('admin/variants/images/<int:id>/delete/', views.admin_variant_image_delete, name='admin_variant_image_delete'),
]
