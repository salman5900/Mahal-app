from django.urls import path
from . import views

app_name = "Houses"

urlpatterns = [
    path("", views.houses, name="houses"),
]