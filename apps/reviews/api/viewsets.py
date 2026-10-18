from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from apps.reviews.selectors import get_reviews
from apps.reviews.services import create_review
from apps.reviews.api.serializers import (
    ReviewListSerializer, ReviewCreateSerializer
)


class ReviewViewSet(
    ListModelMixin, 
    CreateModelMixin, 
    GenericViewSet
):
    queryset = get_reviews()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'product', 'rating','is_verified_purchase'
    )
    serializer_classes = {
        'list':ReviewListSerializer,
        'create':ReviewCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
    
    def perform_create(self, serializer):
        create_review(**serializer.validated_data)