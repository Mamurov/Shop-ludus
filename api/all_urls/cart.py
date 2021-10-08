

from django.urls import path
from api.all_views.cart import *

urlpatterns = [
    path('', CartView.as_view()),
    path('check/', CartCheckView.as_view()),
    path('single/', SingleCartItemView.as_view())
] 