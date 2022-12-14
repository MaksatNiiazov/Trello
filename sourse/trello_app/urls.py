from django.urls import path, include

from trello_app.views import dashboard, register

urlpatterns = [
    path(r"accounts/", include("django.contrib.auth.urls")),
    path(r"dashboard/", dashboard, name="dashboard"),
    # path(r"oauth/", include("social_django.urls")),
    path(r"register/", register, name="register"),
]
