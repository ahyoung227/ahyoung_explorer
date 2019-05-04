from django.shortcuts import render
from places.models import Place
from rest_framework import viewsets
from places.serializers import PlaceSerializer, GeoJSONPlaceSerializer
from django.contrib.gis.geos.point import Point
from django.views.generic import View, TemplateView
from django.contrib.gis.db.models.aggregates import Collect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import Http404

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class GeoJSONPlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = GeoJSONPlaceSerializer

class MapView(TemplateView):
    template_name = "places/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        points = Place.objects.aggregate(c=Collect('location'))['c']
        context['center'] = points.centroid.geojson
        return context

class SmsCreatePlaceView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        msg = request.POST['Body']
        print(msg)
        lat, lng = [float(n) for n in msg.split(',')]
        Place.objects.create(
            name="New Place",
            location=Point((lng, lat), srid=4326)
        )
        print("Created new point at ({}, {})".format(lat, lng))
        return JsonResponse({'status': 'OK'})




