from rest_framework.serializers import ModelSerializer
from apps.catalog.models import Category


class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class CategoryChildSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class CategoryDetailSerializer(ModelSerializer):

    children = CategoryChildSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'children')

