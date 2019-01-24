from django.urls import path
from . import views

urlpatterns = [
	path("", views.level_page, name="level_page"),
]