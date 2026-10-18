from apps.products.selectors import (
    get_featured_products,
    get_hit_products,
    get_home_products,
    get_new_products
)


def get_home_page_data():
    # Данные главной страницы
    return {
        'products': get_home_products(),
        'featured': get_featured_products(),
        'hit_products': get_hit_products(),
        'new_products': get_new_products(), 
    }