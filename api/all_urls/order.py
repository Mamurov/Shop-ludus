from django.urls import path
from ..all_views.order import *


urlpatterns = [
    path('create/', OrderView.as_view())
]