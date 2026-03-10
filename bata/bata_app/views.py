from django.shortcuts import render

def home(request):
    return render(request, 'public/home.html')

def search(request):
    return render(request, 'public/search.html')

def cart(request):
    return render(request, 'public/cart.html')

def profile(request):
    return render(request, 'public/profile.html')

def product(request):
    return render(request, 'public/product.html')

def checkout(request):
    return render(request, 'public/checkout.html')

def orders(request):
    return render(request, 'public/orders.html')

def order_details(request):
    return render(request, 'public/order_details.html')

def addresses(request):
    return render(request, 'public/addresses.html')

def wishlist(request):
    return render(request, 'public/wishlist.html')