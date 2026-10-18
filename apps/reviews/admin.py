from django.contrib import admin
from apps.reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id", "product",
        "name", "rating",
        "is_verified_purchase", "is_active",
        "created_at",
    )
    list_display_links = ("id", "product")
    list_filter = (
        "rating",
        "is_verified_purchase",
        "is_active",
        "created_at",
    )
    search_fields = ("name", "email", "product__name")
    autocomplete_fields = ("product", "user")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "product", "user", "name", "email", "rating",
                )
            },
        ),
        (
            "Отзыв",
            {
                "fields": (
                    "advantages", "disadvantages", "comment",
                )
            },
        ),
        (
            "Статус",
            {
                "fields": (
                    "is_verified_purchase", "is_active",
                )
            },
        ),
        (
            "Дата",
            {
                "fields": (
                    "created_at", "updated_at",
                )
            },
        ),
    )