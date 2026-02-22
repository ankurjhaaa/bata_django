from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, help_text="e.g. #FF0000", blank=True, null=True)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20, help_text="e.g. UK 7, UK 8, US 9")
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

class ProductColorImage(models.Model):
    """
    To store images for different colors of the same shoe.
    e.g. A shoe comes in Black and Brown. Each color will have its own images.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='color_images')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='+')
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False, help_text="Main image for this color")

    def __str__(self):
        return f"{self.product.name} - {self.color.name} Image"

class ProductVariant(models.Model):
    """
    The actual item that a user adds to cart.
    It combines Product + Color + Size + Stock + SKU.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='+')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='+')
    sku = models.CharField(max_length=100, unique=True, help_text="Stock Keeping Unit")
    stock_quantity = models.PositiveIntegerField(default=0)
    price_override = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Leave blank to use product base price")
    
    @property
    def price(self):
        if self.price_override:
            return self.price_override
        return self.product.base_price

    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"

    class Meta:
        verbose_name = 'Product Variant'
        verbose_name_plural = 'Product Variants'
        unique_together = ('product', 'color', 'size')