from django.urls import path, include
from . import views

app_name = "programs"

urlpatterns = [
    path("", views.programs, name="programs_home"),
    path("<int:program_id>/", views.program_detail, name="program_detail"),
]