from rest_framework.serializers import ModelSerializer
from apps.reviews.models import Review


class ReviewListSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'id', 'name', 'rating','advantages', 
            'disadvantages', 'comment',
            'is_verified_purchase', 'created_at'
        )

class ReviewCreateSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'product', 'name', 'email','rating',
            'advantages', 'disadvantages', 'comment'
        )