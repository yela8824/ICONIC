from django.urls import path
from .views import get_icon

urlpatterns = [
    path("<str:theme>/<str:icon_name>", get_icon),
]
