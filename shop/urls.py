from django.urls import path


app_name = "shop"

urlpatterns = [
    path("", main, name="main"),
]
