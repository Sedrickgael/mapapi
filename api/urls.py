from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from . import viewsets


router = DefaultRouter()
router.register('photoapi', viewsets.PhotoViewSet, base_name='photoapi')
router.register('servicesapi', viewsets.ServiceViewSet, base_name='servicesapi')
router.register('salonapi', viewsets.SalonSerializerViewSet, base_name='salonapi')
router.register('coordinateapi', viewsets.CoordinateViewSet, base_name='coordinateapi')


urlpatterns = [
    # path('', views.home , name='home')
]

urlpatterns += router.urls

