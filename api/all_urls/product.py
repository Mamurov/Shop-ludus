

from django.urls import path
from ..all_views.product import ProductCountView, ProductView, ProductSearchView, ProductByIdView

urlpatterns = [
    path('', ProductView.as_view()),
    path('search/<str:query>', ProductSearchView.as_view()),
    path('id/<int:id>', ProductByIdView.as_view()),
    path('count/', ProductCountView.as_view())
]