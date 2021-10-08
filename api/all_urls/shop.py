from django.urls import path
from ..all_views.shop import *

urlpatterns = [
    path('product/', OutShopProductView.as_view()),
    path('check/', CheckIsShopOwnerView.as_view()),
] 