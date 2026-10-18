from django.db.models import Avg, Count, Q 
from apps.reviews.models import Review


def get_product_reviews_stats(product):
    reviews = (
        Review.objects.active()
        .by_product(product)
    )
    stats = reviews.aggregate(
        count=Count('id'),
        avg_rating = Avg('rating'),
        five=Count('id', filter=Q(rating=5)),
        four=Count('id', filter=Q(rating=4)),
        three=Count('id', filter=Q(rating=3)),
        two=Count('id', filter=Q(rating=2)),
        one=Count('id', filter=Q(rating=1)),
    )
    stats['avg_rating']=(
        stats['avg_rating'] or 0
    )
    return stats 


def get_product_rating_percentages(product):
    stats = get_product_reviews_stats(product)
    total = stats['count']
    if not total:
        return {
            'five':0,
            'four':0,
            'three':0,
            'two':0,
            'one':0,
        }
    return {
        'five':round( stats['five'] / total * 100),
        'four':round( stats['four'] / total * 100),
        'three':round( stats['three'] / total * 100),
        'two':round( stats['two'] / total * 100),
        'one':round( stats['one'] / total * 100),
    }


def get_reviews():
    return (
        Review.objects.active().with_related()
    )

def get_verified_reviews():
    return (
        Review.objects.active()
        .verified().with_related()
    )

def get_product_reviews(product):
    return (
        Review.objects.active()
        .by_product(product).with_related()
    )

def get_review_by_id(pk):
    return (
        Review.objects.active()
        .with_related().get(pk=pk)
    )