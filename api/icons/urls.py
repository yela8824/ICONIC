from django.urls import path
from .views import get_icon, index_page, icon_gallery_view, server_error

urlpatterns = [
    path("<str:theme>/<str:icon_name>", get_icon),
    path("", index_page),
    path("gallery/", icon_gallery_view, name="icon-gallery"),
    path("500/", server_error, name="error_500"),
]
