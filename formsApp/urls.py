from django.urls import path
from formsApp.views import homepage_view, login_view, register_view, user_dashboard, form_builder_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("user-dashboard/", user_dashboard, name="user_dashboard"),
    path("form-builder/", form_builder_view, name="form_builder"),
]

urlpatterns += staticfiles_urlpatterns()
