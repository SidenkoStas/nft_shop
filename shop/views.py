from django.shortcuts import render
from django.views.generic import ListView
from shop.models import Item
from django.views import View


def index(request):
    return render(request, "shop/index.html")


def profile(request):
    return render(request, "shop/profile.html")


class ProfileView(ListView):
    model = Item
    template_name = "shop/profile.html"


class AddDropLikes(View):
    pass


def page_not_found(request, exception):
    return render(request, "404.html", status=404)
