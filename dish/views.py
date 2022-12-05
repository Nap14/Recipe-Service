from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import DishForm, DishTypeForm, DishSearchForm
from .models import Chef, Dish, DishType, Product


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={"name": name})

        return context

    def get_queryset(self):

        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)

        return self.queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "dish/dish_detail.html"
    queryset = (
        Dish.objects.all()
        .prefetch_related("dish_type")
        .prefetch_related("ingredients")
        .prefetch_related("cooks")
    )


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = DishForm
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("dish:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("dish:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "dish/dish_confirm_delete.html"
    success_url = reverse_lazy("dish:dish-list")


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 5
    template_name = "dish/product_list.html"


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = "__all__"
    template_name = "dish/product_form.html"
    success_url = reverse_lazy("dish:product-list")


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = "__all__"
    template_name = "dish/product_form.html"
    success_url = reverse_lazy("dish:product-list")


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = "dish/product_confirm_delete.html"
    success_url = reverse_lazy("dish:product-list")


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "dish/dish_type_create_view.html"
    success_url = reverse_lazy("dish:dish-list")
