from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_message", views.add_message),
    path("get_message", views.get_message),
    path("send_email", views.send_email)
]
