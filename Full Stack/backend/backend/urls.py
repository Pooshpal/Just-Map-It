"""
Backend URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("customer/", include("map.urls")),
    path("admin/", admin.site.urls),
]