from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# For swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Obrazci.net API",
      default_version='v1',
      description="API dostop za spletno platformo Obrazci.net",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@obrazci.net"),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include("formsApp.urls")),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    # JWT tokens REST API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

admin.site.index_title = "The formsProject"
admin.site.site_header = "The formsProject Admin"
admin.site.site_title = ""