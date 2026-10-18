from django.db.models import Avg, Count
from apps.reviews.models import Review


def update_product_rating(product):
    stats = product.reviews.filter(
        is_active=True
    ).aggregate(
        rating=Avg('rating'),
        count=Count('id')
    )
    product.rating = (
        stats['rating'] or 0
    )
    product.reviews_count = (
        stats['count'] or 0
    )
    product.save(
        update_fields=[
            'rating', 'reviews_count'
        ]
    )


def create_review(
        *, product, name, email,
        rating, comment, 
        advantages='', disadvantages='',
        user=None
):
    review = Review.objects.create(
        product=product,
        user=user,
        name=name,
        email=email,
        rating=rating,
        comment=comment,
        advantages=advantages,
        disadvantages=disadvantages, 
    )
    update_product_rating(product)
    return review