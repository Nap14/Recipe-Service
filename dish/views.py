from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

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


class ChefListView(LoginRequiredMixin, generic.ListView):
    model = Chef
    queryset = Chef.objects.all().prefetch_related("dishes")
    template_name = "dish/chef_list.html"
    paginate_by = 5


class ChefDetailView(LoginRequiredMixin, generic.DetailView):
    model = Chef
    template_name = "dish/chef_detail.html"
    queryset = Chef.objects.all().prefetch_related("dishes")


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related("ingredients")
    template_name = "dish/dish_list.html"
    paginate_by = 5
