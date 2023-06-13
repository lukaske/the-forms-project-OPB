from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from .views import FormViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet, basename='users')
router.register(r'api/v1/forms', FormViewSet, basename='forms')

urlpatterns = [
    path("", include(router.urls))
]
