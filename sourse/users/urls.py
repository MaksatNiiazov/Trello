from django.urls import path, include

from users.views import activate, register, dashboard

urlpatterns = [
    path(r"accounts/", include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
]
