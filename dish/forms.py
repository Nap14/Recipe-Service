from django import forms
from django.contrib.auth import get_user_model

from dish.models import Dish, Product


class DishForm(forms.ModelForm):

    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"
