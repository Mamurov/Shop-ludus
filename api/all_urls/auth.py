

from django.urls import path
from api.all_views.auth import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('refresh/', RefreshView.as_view())
]