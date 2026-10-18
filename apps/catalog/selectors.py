from apps.catalog.models import Category


def get_categories():
    return (
        Category.objects.active()
        .roots().with_children()
    )


def get_category_by_slug(slug):
    return (
        Category.objects.active()
        .with_children().get(slug=slug)
    )