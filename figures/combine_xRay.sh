convert fig__x-ray-profile-0.8keV-000.png -resize 1334x fig__x-ray-profile-0.8keV-000-resize.png

convert -trim fig__xray_0.8keV_angle_000.png fig__x-ray-profile-0.8keV-000-resize.png -smush 10 fig__xRay.png


rm fig__x-ray-profile-0.8keV-000-resize.png
