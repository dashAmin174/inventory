from django.shortcuts import render

def products(request):
    return render(request, "inventory/products/products.html")

def add_products(request):
    return render(request, "inventory/products/add_products.html")

def materials(request):
    return render(request, "inventory/materials/materials.html")

def add_materials(request):
    return render(request, "inventory/materials/add_materials.html")
