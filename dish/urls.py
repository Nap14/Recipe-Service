from django.urls import path
from .views import (
    index,
    ChefListView,
    ChefDetailView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("chef/", ChefListView.as_view(), name="chef-list"),
    path("chef/<int:pk>/", ChefDetailView.as_view(), name="chef-detail"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("product/", ProductListView.as_view(), name="product-list"),
    path("product/create/", ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
]

app_name = "dish"
