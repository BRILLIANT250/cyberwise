from django.urls import path
from .views import CyberContentAPIView

urlpatterns = [
    path('api/content/', CyberContentAPIView.as_view(), name='content-api'),
]
