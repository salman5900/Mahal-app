from django.urls import path
from . import views

app_name = "Houses"

urlpatterns = [
    path("", views.houses, name="houses"),
    path("house/<int:house_id>/", views.house_detail, name="house_detail"),
]