from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # JSON paths
    path("email", views.email, name="email")
]