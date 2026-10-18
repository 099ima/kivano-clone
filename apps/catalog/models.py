from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from apps.common.models import TimeStampedModel, ActiveModel
from apps.catalog.managers import CategoryManager


class Category(TimeStampedModel,ActiveModel, MPTTModel):
    objects = CategoryManager()
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    ) 

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

