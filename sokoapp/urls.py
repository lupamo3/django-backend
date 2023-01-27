from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet, ArtisanViewSet


router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'artisans', ArtisanViewSet, basename='artisan')


urlpatterns = [
    path('', include(router.urls)),
]
