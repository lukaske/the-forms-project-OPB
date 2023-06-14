from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from .views import FormViewSet, UserViewSet, SubmitViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet, basename='users')
router.register(r'api/v1/forms', FormViewSet, basename='forms')
router.register(r'api/v1/submits', SubmitViewSet, basename='forms')

urlpatterns = [
    path("", include(router.urls))
]
