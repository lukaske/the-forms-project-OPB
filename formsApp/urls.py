from django.urls import path
from formsApp.views import homepage_view, login_view, register_view, user_dashboard, form_builder_view, dynamic_form_view, logout_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("user-dashboard/", user_dashboard, name="user_dashboard"),
    path('form_viewer/<str:view_name>/', dynamic_form_view, name='dynamic_form_view'),
    path("form-builder/", form_builder_view, name="form_builder"),
    path('logout/', logout_view, name='logout')
]

urlpatterns += staticfiles_urlpatterns()
