from django.db import models
from apps.common.models import TimeStampedModel, ActiveModel
from apps.products.managers import ProductManager
from apps.catalog.models import Category


class Brand(TimeStampedModel, ActiveModel):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True) 

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Бренды'
        verbose_name = 'бренд'
    
    def __str__(self):
        return self.name
    

class StockStatus(models.TextChoices):
    IN_STOCK = 'in_stock', 'в наличии'
    OUT_OF_STOCK = 'out_of_stock', 'Нет в наличии'
    PRE_ORDER = 'pre_order', 'Предзаказ'
    EXPECTED = 'expected', 'Ожидается'


class Product(TimeStampedModel, ActiveModel):
    objects = ProductManager()
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        related_name='products'
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT,
        related_name='products'
    )
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(unique=True)
    sku = models.CharField(
        max_length=100, unique=True, 
        help_text='i20260626', verbose_name='Артикул'
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена")
    old_price = models.DecimalField(
        max_digits=12, decimal_places=2, 
        blank=True, null=True, verbose_name="Старая цена"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Рекомендумый")
    is_new = models.BooleanField(default=False, verbose_name="Новинка")
    is_hit = models.BooleanField(default=False, verbose_name="Хит продаж")
    warranty = models.PositiveSmallIntegerField(
        default=12, help_text='В месяцах', verbose_name="Гарантия (месяцев)"
    )
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, default=0
    )
    reviews_count = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(
        default=0, null=True,
        verbose_name="Количество на складе"
    )
    stock_status = models.CharField(
        max_length=20, choices=StockStatus.choices,
        default=StockStatus.IN_STOCK,
        verbose_name='Статус наличия'
    )
    views_count = models.PositiveIntegerField(
        default=0, editable=False,
        verbose_name='Количество просмотров'
    )

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Товары'
        verbose_name = 'товар'

        indexes = [
            models.Index(fields=['is_active', 'category']),
            models.Index(fields=['is_active', 'brand'])
        ]
    
    def __str__(self):
        return self.name


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')
    is_main = models.BooleanField(default=False) 

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.product.name


class Attribute(models.Model):
    # цвет, память, ОЗУ, Диагональ, Мощность
    TEXT = 'text'
    SELECT = 'select'
    TYPE_CHOICES = (
        (TEXT, 'Текст'),
        (SELECT, 'Список'),
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name='attributes'
    )
    name = models.CharField(max_length=150)
    attribute_type = models.CharField(
        max_length=20, choices=TYPE_CHOICES,
        default=TEXT
    )
    is_filterable = models.BooleanField(default=True)

    class Meta:
        verbose_name='характеристика'
        verbose_name_plural='Характеристики'

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    # черный, белый, зеленый | 256гб, 16 дюймов
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE,
        related_name='values' 
    )
    value = models.CharField(max_length=150)

    class Meta:
        verbose_name='значение характеристики'
        verbose_name_plural='Значения характеристики'

    def __str__(self):
        return self.value


class ProductAttribute(models.Model):
    # связь товара со значениями
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='attributes'
    )
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE,
        related_name='product_attributes'
    )
    value = models.ForeignKey(
        AttributeValue, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='product_attributes'
    )
    text_value = models.CharField(
        max_length=155, blank=True
    )

    class Meta:
        verbose_name='Характеристика товара'
        verbose_name_plural='Характеристики товаров'

    def __str__(self):
        return f'{self.product.name} - {self.attribute.name}'