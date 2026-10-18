from django.db import models
from apps.products.querysets import ProductQuerySet

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def active(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured()
    
    def hits(self):
        return self.get_queryset().hits()
    
    def news(self):
        return self.get_queryset().news()
    
    def with_related(self):
        return self.get_queryset().with_related()