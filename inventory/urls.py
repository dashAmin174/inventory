from django.urls import path
from .views import products, add_products, materials, add_materials


urlpatterns = [
    path("products/", products, name = "products"),
    path("add_products/", add_products, name = "add_products"),
    path("materials/", materials, name = "materials"),
    path("add_materials/", add_materials, name = "add_materials"),
]