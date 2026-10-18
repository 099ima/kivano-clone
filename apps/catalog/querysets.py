from django.db import models


class CategoryQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True)
    
    def roots(self):
        return self.filter(parent=None)
    
    def with_children(self):
        return self.prefetch_related('children')
    