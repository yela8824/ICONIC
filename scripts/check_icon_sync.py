import os
import sys

dark_path = "icons/dark"
light_path = "icons/light"

dark_svgs = set(f for f in os.listdir(dark_path) if f.endswith(".svg"))
light_svgs = set(f for f in os.listdir(light_path) if f.endswith(".svg"))

missing_in_light = dark_svgs - light_svgs
missing_in_dark = light_svgs - dark_svgs

if missing_in_light or missing_in_dark:
    print("❌ Icons are not in sync!")
    if missing_in_light:
        print(f"Icons missing in light/: {sorted(missing_in_light)}")
    if missing_in_dark:
        print(f"Icons missing in dark/: {sorted(missing_in_dark)}")
    sys.exit(1)
else:
    print("✅ All icons are synced between dark/ and light/")

