from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('product/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('order-details/', views.order_details, name='order_details'),
    path('addresses/', views.addresses, name='addresses'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
