from django.urls import path
from apps.products.views import HomeView

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
