from rest_framework.response import Response

from django.urls import path
from api.all_views.catalog import *


urlpatterns = [
    path('all/', CatalogView.as_view()),
]