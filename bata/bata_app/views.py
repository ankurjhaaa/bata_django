from django.shortcuts import render

def home(request):
    return render(request, 'public/home.html')

def search(request):
    return render(request, 'public/search.html')

def cart(request):
    return render(request, 'public/cart.html')

def profile(request):
    return render(request, 'public/profile.html')