convert fig__xray_0.8keV_observed.png -resize 1100x fig__xray_0.8keV_observed-resize.png

convert -size 1320x1200 \
        -page 0x0 fig__xray_0.8keV_observed-resize.png  \
        -page 50x50 fig__xray_0.8keV_angle_000.png  \
        -layers flatten  fig__xRayMap.png

rm fig__xray_0.8keV_observed-resize.png
