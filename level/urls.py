from django.urls import path
from . import views

urlpatterns = [
	path("general-information/", views.level_general, name="level_general"),
	path("tank-material/", views.level_tank, name="level_tank"),
]