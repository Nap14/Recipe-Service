from django.shortcuts import render
from .models import Chef, Dish, DishType


def index(request):
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "chefs": Chef.objects.count(),
        "dishes": Dish.objects.count(),
        "types": DishType.objects.count(),
        "num_visits": num_visits + 1,
    }

    return render(request, "dish/index.html", context=context)
