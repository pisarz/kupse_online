from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (
    HomeView,
    OrderSummaryView,
    CheckoutView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
)

app_name = 'core'

urlpatterns = [
    path('', cache_page(60 * 60)(HomeView.as_view()), name='home'),
    path('checkout/', cache_page(60 * 60)(CheckoutView.as_view()), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', cache_page(60 * 60)(ItemDetailView.as_view()), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart,
         name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-from-cart')
]
