from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    OrderingFilter, SearchFilter
)
from apps.products.api.filters import ProductFilter
from apps.common.api.viewsets import BaseReadOnlyModelViewSet
from apps.products.selectors import get_products
from apps.products.api.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
)

class ProductViewSet(BaseReadOnlyModelViewSet):
    lookup_field = 'slug' 
    serializer_classes = {
        'list': ProductListSerializer,
        'retrieve': ProductDetailSerializer,
    }
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter, 
        SearchFilter
    )
    filterset_class = ProductFilter
    search_fields = (
        'name', 'sku', 'description',
        'brand__name', 'category__name'
    )
    ordering_fields = (
        'price', 'created_at', 'name'
    )
    ordering = ('-created_at',)

    def get_queryset(self):
        return get_products()
