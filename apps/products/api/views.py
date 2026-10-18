from rest_framework.generics import RetrieveAPIView
from apps.products.selectors import get_products
from .serializers import ProductDetailSerializer


class ProductByIdAPIView(RetrieveAPIView):
    queryset = get_products()
    serializer_class = ProductDetailSerializer