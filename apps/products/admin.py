from django.contrib import admin
from apps.products.models import (
        Brand, Product, ProductImage, 
        Attribute, AttributeValue, ProductAttribute
    )

admin.site.register(Attribute)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('value', 'attribute')
    list_filter = ('attribute',)
    search_fields = ('value',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 
                    'price', 'stock_status', 'is_active')
    list_filter = ('category', 'brand', 'is_active')
    search_fields = ('name', 'sku')
    prepopulated_fields = {'slug':('name',)}
    inlines = [ProductImageInline, ProductAttributeInline]


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute', 'value')
    list_filter = ('attribute',)
    search_fields = ('product__name',)