"""ahyoung_explorer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.gis import admin
from django.urls import path, include
from rest_framework import routers
from places import views

router = routers.DefaultRouter()
router.register('places', views.PlaceViewSet)
router.register('geo_places', views.GeoJSONPlaceViewSet)

urlpatterns = [
    path('', views.MapView.as_view(), name='home'),
    path('sms', views.SmsCreatePlaceView.as_view(), name='sms'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
