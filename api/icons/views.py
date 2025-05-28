from django.http import FileResponse, Http404
import os
from django.conf import settings

ICON_PATH = os.path.abspath(os.path.join(settings.BASE_DIR, "..", "icons"))


def get_icon(request, theme, icon_name):
    if theme not in ["dark", "light"]:
        raise Http404(f"Invalid theme: {theme}")

    file_path = os.path.join(ICON_PATH, theme, f"{icon_name}.svg")

    if not os.path.exists(file_path):
        raise Http404("Icon not found")

    return FileResponse(open(file_path, "rb"), content_type="image/svg+xml")
