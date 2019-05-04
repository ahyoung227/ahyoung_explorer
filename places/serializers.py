from rest_framework_gis import serializers
from places.models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'why', 'suggestion', 'feedback')

class GeoJSONPlaceSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'location', 'why', 'suggestion', 'feedback')
        geo_field = "location"
