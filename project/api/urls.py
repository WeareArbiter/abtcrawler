from django.conf.urls import url
from project.api.views import RequestFormAPIView

urlpatterns = [
    url(r'^request-api/$', RequestFormAPIView.as_view(), name='request-api'),
    ]
