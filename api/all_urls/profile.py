
from django.urls import path
from ..all_views.profile import ProfileView


urlpatterns = [
    path('', ProfileView.as_view())
]