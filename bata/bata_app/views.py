from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'public/home.html')

def search(request):
    return render(request, 'public/search.html')

def product(request):
    return render(request, 'public/product.html')

# --- Authentication Views ---

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    error = None
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid username or password"
            
    return render(request, 'auth/login.html', {'error': error})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    error = None
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        u = request.POST.get('username')
        p1 = request.POST.get('password')
        p2 = request.POST.get('password_confirm')
        
        if p1 != p2:
            error = "Passwords do not match."
        elif User.objects.filter(username=u).exists():
            error = "Username already exists."
        elif User.objects.filter(email=email).exists():
            error = "Email already exists."
        else:
            user = User.objects.create_user(username=u, email=email, password=p1, first_name=fname, last_name=lname)
            login(request, user)
            return redirect('home')
            
    return render(request, 'auth/signup.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')

# --- Protected Views ---

@login_required
def cart(request):
    return render(request, 'public/cart.html')

@login_required
def profile(request):
    return render(request, 'public/profile.html')

@login_required
def checkout(request):
    return render(request, 'public/checkout.html')

@login_required
def orders(request):
    return render(request, 'public/orders.html')

@login_required
def order_details(request):
    return render(request, 'public/order_details.html')

@login_required
def addresses(request):
    return render(request, 'public/addresses.html')

@login_required
def wishlist(request):
    return render(request, 'public/wishlist.html')