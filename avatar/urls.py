from django.urls import path
from .views import get_avatar

urlpatterns = [
    path('avatar/', get_avatar, name='avatar')
]
