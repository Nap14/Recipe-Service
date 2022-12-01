from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dish.models import DishType, Dish, Product, Chef


@admin.register(Chef)
class ChefAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("additional info", {"fields": ("first_name", "last_name")}),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "dish_type",
        "created_data",
    ]
    search_fields = ("name",)
    list_filter = ("dish_type",)


admin.site.register(DishType)
