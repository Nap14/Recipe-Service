from django.urls import path
from .views import (
    index,
    ChefListView,
    ChefDetailView,
    DishListView,
    DishDetailView,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("chef/", ChefListView.as_view(), name="chef-list"),
    path("chef/<int:pk>/", ChefDetailView.as_view(), name="chef-detail"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
]

app_name = "dish"
