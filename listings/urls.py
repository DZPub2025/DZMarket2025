from rest_framework import routers
from .views import AdViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'ads', AdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from .views_images import AdImageUploadView, AdImageDeleteView

from django.urls import re_path

urlpatterns += [
    re_path(r'^ads/(?P<ad_id>\d+)/images/$', AdImageUploadView.as_view(), name='ad-image-upload'),
    re_path(r'^ads/(?P<ad_id>\d+)/images/(?P<pk>\d+)/$', AdImageDeleteView.as_view(), name='ad-image-delete'),
]
