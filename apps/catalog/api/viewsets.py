from apps.common.api.viewsets import BaseReadOnlyModelViewSet
from apps.catalog.selectors import (
    get_categories, get_category_by_slug
)
from apps.catalog.api.serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer
)


class CategoryViewSet(BaseReadOnlyModelViewSet):
    
    lookup_field = 'slug'
    serializer_classes = {
        'list': CategoryListSerializer,
        'retrieve': CategoryDetailSerializer,
    }

    def get_queryset(self):
        return get_categories()
    
    def get_object(self):
        return get_category_by_slug(
            self.kwargs['slug']
        )