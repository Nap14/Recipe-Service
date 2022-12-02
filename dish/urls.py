from django.urls import path
from .views import (
    index,
    ChefListView,
    ChefDetailView,
    DishListView,
    DishDetailView,
    DishCreateView,
    ProductListView,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("chef/", ChefListView.as_view(), name="chef-list"),
    path("chef/<int:pk>/", ChefDetailView.as_view(), name="chef-detail"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("product/", ProductListView.as_view(), name="product-list"),
]

app_name = "dish"
