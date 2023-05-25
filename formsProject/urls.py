from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("formsApp.urls")),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]

admin.site.index_title = "The formsProject"
admin.site.site_header = "The formsProject Admin"
admin.site.site_title = ""