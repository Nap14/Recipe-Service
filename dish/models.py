from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Chef(AbstractUser):
    class Meta:
        ordering = ["username"]
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username}"


class DishType(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):

    UNITS_OF_MEASUREMENT = (
        ("g", "grams"),
        ("u", "units"),
        ("ml", "milliliters"),
    )

    name = models.CharField(max_length=255, unique=True)
    units = models.CharField(max_length=5, choices=UNITS_OF_MEASUREMENT)

    def __str__(self):
        return f"{self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    created_data = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=50, blank=True)
    steps = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    dish_type = models.ForeignKey(
        "DishType", on_delete=models.SET_NULL, related_name="dishes", null=True,
    )
    ingredients = models.ManyToManyField(Product, blank=True)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"
