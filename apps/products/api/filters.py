import django_filters
from apps.products.models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )
    category = django_filters.NumberFilter(
        field_name='category__id'
    )
    category_slug = django_filters.CharFilter(
        field_name='category__slug'
    )
    brand = django_filters.NumberFilter(
        field_name='brand__id'
    )
    brand_slug = django_filters.CharFilter(
        field_name='brand__slug'
    )
    sku = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    stock_status = django_filters.CharFilter()
    is_new = django_filters.BooleanFilter()
    is_hit = django_filters.BooleanFilter()
    is_featured = django_filters.BooleanFilter()
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Product
        fields = []