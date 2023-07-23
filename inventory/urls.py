from .views import (inventory, products, add_products, materials, add_materials,
    js_add_products, js_update_products, js_add_materials, js_update_materials,
    add_products_cardex, add_materials_cardex, ProductsViewSet, MaterialsViewSet,
    ProductsCardexViewSet, MaterialsCardexsViewSet, product_cardex_export_to_excel,
    material_cardex_export_to_excel, product_cardex_export_to_pdf, material_cardex_export_to_pdf)
from django.urls import path


urlpatterns = [
    path("material_cardex_excel/<code>", material_cardex_export_to_excel, name = "material_cardex_excel"),
    path("product_cardex_excel/<code>", product_cardex_export_to_excel, name = "product_cardex_excel"),
    path("material_cardex_pdf/<code>", material_cardex_export_to_pdf, name = "material_cardex_pdf"),
    path('api/materials_cardex', MaterialsCardexsViewSet.as_view(), name = 'materials_cardex_api'),
    path("product_cardex_pdf/<code>", product_cardex_export_to_pdf, name = "product_cardex_pdf"),
    path('api/products_cardex', ProductsCardexViewSet.as_view(), name = 'products_cardex_api'),
    path("js_update_materials", js_update_materials, name = "js_update_materials"),
    path("js_update_products", js_update_products, name = "js_update_products"),
    path("materials/<code>", add_materials_cardex, name = "materials_cardex"),
    path('api/materials', MaterialsViewSet.as_view(), name = 'materials_api'),
    path("products/<code>", add_products_cardex, name = "products_cardex"),
    path('api/products', ProductsViewSet.as_view(), name = 'products-api'),
    path("js_add_materials", js_add_materials, name = "js_add_materials"),
    path("js_add_products", js_add_products, name = "js_add_products"),
    path("add_materials/", add_materials, name = "add_materials"),
    path("add_products/", add_products, name = "add_products"),
    path("materials/", materials, name = "materials"),
    path("products/", products, name = "products"),
    path("", inventory, name = "inventory")
]