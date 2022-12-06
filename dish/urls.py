from django.urls import path
from .views import (
    index,
    registration_success_view,
    ChefListView,
    ChefDetailView,
    ChefCreateView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    DishTypeCreateView,
    DishDeleteView,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("chef/", ChefListView.as_view(), name="chef-list"),
    path("chef/<int:pk>/", ChefDetailView.as_view(), name="chef-detail"),
    path("chef/create/", ChefCreateView.as_view(), name="chef-create"),
    path("chef/succes/", registration_success_view, name="chef-success"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("product/", ProductListView.as_view(), name="product-list"),
    path("product/create/", ProductCreateView.as_view(), name="product-create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"
    ),
    path("dish-type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
]

app_name = "dish"
