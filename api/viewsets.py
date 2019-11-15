from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from . import models
from . import serializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class PhotoViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Photo.objects.all()
    serializer_class = serializer.PhotoSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Service.objects.all()
    serializer_class = serializer.ServiceSerializer


class SalonSerializerViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Salon.objects.all()
    serializer_class = serializer.SalonSerializer


class CoordinateViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Coordinate.objects.all()
    serializer_class = serializer.CoordinateSerializer
