

from django.urls import path, include

urlpatterns = [
    path('product/', include('api.all_urls.product')),
    path('auth/', include('api.all_urls.auth')),
    path('catalog/', include('api.all_urls.catalog')),
    path('shop/', include('api.all_urls.shop')),
    path('profile/', include('api.all_urls.profile')),
    path('shop/', include('api.all_urls.shop')),
    path('cart/', include('api.all_urls.cart')),
    path('purchases/', include('api.all_urls.order'))
]
