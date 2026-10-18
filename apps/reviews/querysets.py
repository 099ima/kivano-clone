from django.db import models


class ReviewQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True)

    def verified(self):
        return self.filter(
            is_verified_purchase=True
        )

    def with_related(self):
        return self.select_related(
            "product",
            "user",
        )

    def by_product(self, product):
        return self.filter(
            product=product
        )

    def by_rating(self, rating):
        return self.filter(rating=rating)