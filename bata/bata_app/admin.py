from django.contrib import admin
from .models import Category, Product, ProductVariant, ProductColorImage, Color, Size

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductColorImage)
admin.site.register(Color)
admin.site.register(Size)