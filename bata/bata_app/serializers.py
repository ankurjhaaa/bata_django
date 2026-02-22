from rest_framework import serializers
from .models import Category, Product, ProductVariant, ProductColorImage, Color, Size

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ProductColorImageSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    class Meta:
        model = ProductColorImage
        fields = ['id', 'color', 'image', 'is_main']

class ProductVariantSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    
    class Meta:
        model = ProductVariant
        fields = ['id', 'color', 'size', 'sku', 'stock_quantity', 'price_override', 'price']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    color_images = ProductColorImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'category', 'base_price', 'is_active', 'created_at', 'updated_at', 'variants', 'color_images']
