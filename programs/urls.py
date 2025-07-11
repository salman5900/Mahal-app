from django.urls import path, include
from . import views

app_name = "programs"

urlpatterns = [
    path("", views.programs, name="programs_home"),
]