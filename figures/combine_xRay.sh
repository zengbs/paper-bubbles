convert fig__xray_0.8keV_observed.png -resize 945x470! fig__xray_0.8keV_observed-resize.png


composite -geometry +120+512  fig__xray_0.8keV_observed-resize.png  fig__xray_0.8keV_angle_000.png fig__xraymap.png
