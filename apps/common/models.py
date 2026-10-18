from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    is_active = models.BooleanField(
        default=True, verbose_name="Активен"
    ) 

    class Meta:
        abstract = True