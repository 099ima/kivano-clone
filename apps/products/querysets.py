from django.db import models
from django.db.models import Prefetch


class ProductQuerySet(models.QuerySet):
    
    def active(self):
        return self.filter(is_active=True)

    def featured(self):
        return self.filter(is_featured=True)
    
    def hits(self):
        return self.filter(is_hit=True)
    
    def news(self):
        return self.filter(is_new=True)
    
    def in_stock(self):
        return self.filter(stock__gt=0)
    
    def with_related(self):
        return self.select_related(
            'category', 'brand'
        ).prefetch_related('images',)
    
    
    def detail(self):
        
        from apps.products.models import ProductAttribute

        return (
            self.select_related('category', 'brand')
            .prefetch_related('images', 
                Prefetch(
                    'attributes',
                    queryset=ProductAttribute.objects.select_related(
                        'attribute'
                    ),
                ),
            )
        )