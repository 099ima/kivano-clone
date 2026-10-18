from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.catalog.api.viewsets import CategoryViewSet
from apps.products.api.viewsets import ProductViewSet
from apps.products.api.views import ProductByIdAPIView
from apps.reviews.api.viewsets import ReviewViewSet

router  = DefaultRouter()

router.register('products', ProductViewSet, basename='products')

router.register('categories', CategoryViewSet, basename='categories')

router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('products/id/<int:pk>/', ProductByIdAPIView.as_view(), name='product-by-id'),
]

urlpatterns += router.urls
 


 