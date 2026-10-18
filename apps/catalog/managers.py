from django.db import models
from apps.catalog.querysets import CategoryQuerySet


class CategoryManager(models.Manager):

    def get_queryset(self):
        return CategoryQuerySet(
            self.model, using=self._db
        )

    def active(self):
        return self.get_queryset().active()
    
    def roots(self):
        return self.get_queryset().roots()
    
    def with_children(self):
        return self.get_queryset().with_children()