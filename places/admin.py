from django.contrib.gis import admin
from places.models import Place

admin.site.register(Place, admin.OSMGeoAdmin)
