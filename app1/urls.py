from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from django.views.generic import RedirectView

from .views import index, UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # url(r'^$', index),
    path('', include(router.urls)),
    url(r'^$', RedirectView.as_view(url='/api/auth/login/')),
]
