from django.db import models

from apps.reviews.querysets import ReviewQuerySet


class ReviewManager(models.Manager):

    def get_queryset(self):
        return ReviewQuerySet(
            self.model, using=self._db,
        )

    def active(self):
        return self.get_queryset().active()

    def verified(self):
        return self.get_queryset().verified()

    def with_related(self):
        return self.get_queryset().with_related()

    def by_product(self, product):
        return self.get_queryset().by_product(product)

    def by_rating(self, rating):
        return self.get_queryset().by_rating(rating)