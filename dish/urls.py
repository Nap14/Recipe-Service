from django.urls import path
from .views import (
    index,
    ChefListView,
    ChefDetailView,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("chef/", ChefListView.as_view(), name="chef-list"),
    path("chef/<int:pk>/", ChefDetailView.as_view(), name="chef-detail")
]

app_name = "dish"
