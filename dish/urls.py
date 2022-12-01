from django.urls import path
from .views import (
    index,
    ChefListView
)

urlpatterns = [
    path("", index, name="home_page"),
    path("chef/", ChefListView.as_view(), name="chef-list"),
]

app_name = "dish"
