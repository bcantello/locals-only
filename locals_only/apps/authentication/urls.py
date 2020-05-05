from django.conf.urls import url
from apps.authentication.views import RegistrationAPIView, LoginApiView

urlpatterns = [
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginApiView.as_view(), name='login'),
]
