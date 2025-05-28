from django.urls import path
from .views import get_icon, index_page

urlpatterns = [
    path("<str:theme>/<str:icon_name>", get_icon),
    path("", index_page),
]
