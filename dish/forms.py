from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)

from dish.models import Dish, Product, DishType, Chef


class ChefCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name")


class DishForm(forms.ModelForm):

    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."}),
    )


class DishTypeForm(forms.ModelForm):

    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 20

    name = forms.CharField(
        required=True,
        validators=(
            MinLengthValidator(
                NAME_MIN_LENGTH, message=f"Min length for this field {NAME_MIN_LENGTH}"
            ),
            MaxLengthValidator(
                NAME_MAX_LENGTH, message=f"Max length for this field {NAME_MAX_LENGTH}"
            ),
            RegexValidator(
                regex=r"^[A-Z]{1}[a-z]+", message="Must starts with upper case word"
            ),
        ),
    )

    class Meta:
        model = DishType
        fields = ("name",)


class ProductSearchForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."}),
    )
