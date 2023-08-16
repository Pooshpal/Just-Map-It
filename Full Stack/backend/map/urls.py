from django.urls import path,include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'lists', views.ListView, 'view')

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("list/", include(router.urls), name="list"),
]