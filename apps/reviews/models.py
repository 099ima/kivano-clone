from django.conf import settings
from django.db import models
from apps.common.models import (
    ActiveModel, TimeStampedModel
)
from apps.products.models import Product
from apps.reviews.managers import ReviewManager


class Review(TimeStampedModel, ActiveModel):
    objects = ReviewManager()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True, 
        related_name='reviews'
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    rating = models.PositiveSmallIntegerField()
    advantages = models.TextField(blank=True, verbose_name='Преимущества')
    disadvantages = models.TextField(blank=True, verbose_name='Недостатки')
    comment = models.TextField()
    is_verified_purchase = models.BooleanField(
        default=False, verbose_name='подтверждение покупка'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Отзывы'
        verbose_name = 'отзыв'