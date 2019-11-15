from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from . import models
from django.contrib.auth.models import User


class PhotoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'


class ServiceSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class SalonSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    Services_salons = ServiceSerializer(many=True,  read_only=True, required=False )

    photo_salon = PhotoSerializer(many=True,  read_only=True, required=False)
    
    class Meta:
        model = models.Salon
        fields = '__all__'
        depth = 1

class CoordinateSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    coordonnees_salon = SalonSerializer(many=True,  read_only=True, required=False)


    class Meta:
        model = models.Coordinate
        fields = '__all__'

