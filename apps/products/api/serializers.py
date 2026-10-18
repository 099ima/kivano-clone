from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from apps.reviews.selectors import get_product_reviews_stats
from apps.catalog.models import Category
from apps.products.models import (
    Product, Brand, ProductImage, ProductAttribute,
    Attribute, 
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id','name', 'slug'
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id','image', 'is_main'
        )


class AttributeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attribute
        fields = ('id', 'name')


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)

    class Meta:
        model = ProductAttribute
        fields = ('attribute', 'value')


class ProductListSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'price',
            'old_price', 'brand'
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    images = ProductImageSerializer(
        many=True, read_only=True
    )
    attributes = ProductAttributeSerializer(
        many=True, read_only=True
    )
    reviews_stats = SerializerMethodField()

    def get_reviews_stats(self, obj):
        return get_product_reviews_stats(obj)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'description',
            'category', 'brand',
            'images', 'attributes',
            'price', 'old_price',
            'stock_status', 'views_count', 'warranty'
            'rating', 'reviews_count', 'reviews_stats'
        )