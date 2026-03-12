from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from .models import Color, Size, ProductVariant, VariantImage


def home(request):
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True).prefetch_related('variants', 'variants__images')[:8]
    return render(request, 'public/home.html', {
        'categories': categories,
        'products': products
    })

def search(request):
    q = request.GET.get('q', '')
    if q:
        products = Product.objects.filter(is_active=True, name__icontains=q).prefetch_related('variants', 'variants__images')
    else:
        products = Product.objects.filter(is_active=True).prefetch_related('variants', 'variants__images')
    return render(request, 'public/search.html', {'products': products, 'q': q})

def product(request, slug):
    product = Product.objects.get(slug=slug, is_active=True)
    variants = product.variants.all().prefetch_related('images')
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id).prefetch_related('variants', 'variants__images')[:4]
    
    return render(request, 'public/product.html', {
        'product': product,
        'variants': variants,
        'related_products': related_products
    })


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


def admin_dashboard(request):
    categories_count = Category.objects.count()
    products_count = Product.objects.count()
    return render(request, 'admin_custom/dashboard.html', {
        'categories_count': categories_count,
        'products_count': products_count
    })

def admin_categories(request):
    categories = Category.objects.all().order_by('-created_at')
    return render(request, 'admin_custom/categories/list.html', {'categories': categories})

def admin_category_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        parent_id = request.POST.get('parent')
        description = request.POST.get('description')
        is_active = request.POST.get('is_active') == 'on'
        image = request.FILES.get('image')

        parent = Category.objects.filter(id=parent_id).first() if parent_id else None

        Category.objects.create(
            name=name, slug=slug, parent=parent, 
            description=description, is_active=is_active, image=image
        )
        return redirect('admin_categories')
    
    return render(request, 'admin_custom/categories/form.html', {'categories': categories})

def admin_category_edit(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug')
        parent_id = request.POST.get('parent')
        category.parent = Category.objects.filter(id=parent_id).first() if parent_id else None
        category.description = request.POST.get('description')
        category.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('image'):
            category.image = request.FILES.get('image')
            
        category.save()
        return redirect('admin_categories')

    return render(request, 'admin_custom/categories/form.html', {'category': category, 'categories': categories})

def admin_category_delete(request, id):
    if request.method == 'POST':
        Category.objects.filter(id=id).delete()
    return redirect('admin_categories')

def admin_products(request):
    products = Product.objects.all().select_related('category').order_by('-created_at')
    return render(request, 'admin_custom/products/list.html', {'products': products})

def admin_product_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        is_active = request.POST.get('is_active') == 'on'

        category = Category.objects.filter(id=category_id).first()

        Product.objects.create(
            name=name, slug=slug, category=category,
            description=description, is_active=is_active
        )
        return redirect('admin_products')
    
    return render(request, 'admin_custom/products/form.html', {'categories': categories})

def admin_product_edit(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.slug = request.POST.get('slug')
        category_id = request.POST.get('category')
        product.category = Category.objects.filter(id=category_id).first()
        product.description = request.POST.get('description')
        product.is_active = request.POST.get('is_active') == 'on'
        
        product.save()
        return redirect('admin_products')

    return render(request, 'admin_custom/products/form.html', {'product': product, 'categories': categories})

def admin_product_delete(request, id):
    if request.method == 'POST':
        Product.objects.filter(id=id).delete()
    return redirect('admin_products')






def admin_colors(request):
    colors = Color.objects.all().order_by('name')
    return render(request, 'admin_custom/colors/list.html', {'colors': colors})

def admin_color_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hex_code = request.POST.get('hex_code')
        Color.objects.create(name=name, hex_code=hex_code)
        return redirect('admin_colors')
    return render(request, 'admin_custom/colors/form.html')

def admin_color_edit(request, id):
    color = Color.objects.get(id=id)
    if request.method == 'POST':
        color.name = request.POST.get('name')
        color.hex_code = request.POST.get('hex_code')
        color.save()
        return redirect('admin_colors')
    return render(request, 'admin_custom/colors/form.html', {'color': color})

def admin_color_delete(request, id):
    if request.method == 'POST':
        Color.objects.filter(id=id).delete()
    return redirect('admin_colors')

# --- Size CRUD ---
def admin_sizes(request):
    sizes = Size.objects.all().order_by('name')
    return render(request, 'admin_custom/sizes/list.html', {'sizes': sizes})

def admin_size_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Size.objects.create(name=name)
        return redirect('admin_sizes')
    return render(request, 'admin_custom/sizes/form.html')

def admin_size_edit(request, id):
    size = Size.objects.get(id=id)
    if request.method == 'POST':
        size.name = request.POST.get('name')
        size.save()
        return redirect('admin_sizes')
    return render(request, 'admin_custom/sizes/form.html', {'size': size})

def admin_size_delete(request, id):
    if request.method == 'POST':
        Size.objects.filter(id=id).delete()
    return redirect('admin_sizes')





def admin_variant_create(request, product_id):
    product = Product.objects.get(id=product_id)
    colors = Color.objects.all()
    sizes = Size.objects.all()
    if request.method == 'POST':
        color_id = request.POST.get('color')
        size_id = request.POST.get('size')
        sku = request.POST.get('sku')
        stock = request.POST.get('stock_quantity')
        price = request.POST.get('price')
        color = Color.objects.get(id=color_id)
        size = Size.objects.get(id=size_id)
        variant = ProductVariant.objects.create(product=product, color=color, size=size, sku=sku, stock_quantity=stock, price=price)
        return redirect('admin_variant_edit', id=variant.id)
    return render(request, 'admin_custom/variants/form.html', {'product': product, 'colors': colors, 'sizes': sizes})

def admin_variant_edit(request, id):
    variant = ProductVariant.objects.get(id=id)
    colors = Color.objects.all()
    sizes = Size.objects.all()
    images = variant.images.all()
    
    if request.method == 'POST':
        if 'update_variant' in request.POST:
            color_id = request.POST.get('color')
            size_id = request.POST.get('size')
            variant.sku = request.POST.get('sku')
            variant.stock_quantity = request.POST.get('stock_quantity')
            variant.price = request.POST.get('price')
            variant.color = Color.objects.get(id=color_id)
            variant.size = Size.objects.get(id=size_id)
            variant.save()
            return redirect('admin_product_edit', id=variant.product.id)
        elif 'upload_image' in request.POST:
            image_file = request.FILES.get('image')
            is_main = request.POST.get('is_main') == 'on'
            if is_main:
                VariantImage.objects.filter(variant=variant).update(is_main=False)
            if image_file:
                VariantImage.objects.create(variant=variant, image=image_file, is_main=is_main)
            return redirect('admin_variant_edit', id=variant.id)
            
    return render(request, 'admin_custom/variants/form.html', {'variant': variant, 'product': variant.product, 'colors': colors, 'sizes': sizes, 'images': images})

def admin_variant_delete(request, id):
    if request.method == 'POST':
        variant = ProductVariant.objects.get(id=id)
        product_id = variant.product.id
        variant.delete()
        return redirect('admin_product_edit', id=product_id)
    return redirect('admin_products')

def admin_variant_image_delete(request, id):
    if request.method == 'POST':
        image = VariantImage.objects.get(id=id)
        variant_id = image.variant.id
        image.delete()
        return redirect('admin_variant_edit', id=variant_id)
    return redirect('admin_products')
