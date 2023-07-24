from .serializers import (ProductsSerializer, MaterialsSerializer, ProductsCardexSerializer, MaterialsCardexsSerializer)
from .models import (Products, Materials, ProductsCardex, MaterialsCardex)
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, filters
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from django.shortcuts import render
from reportlab.lib import colors
from root.local import BASE_DIR
from openpyxl import Workbook
import os


''' Create rest api views '''
class ProductsViewSet(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    ordering_fields = ['product_author', 'product_name', 'product_code', 'product_color', 'product_quantity', 'product_location', 'product_hall', 'product_unit', 'product_date', 'is_active', 'is_available',]
    search_fields = ['product_code', 'product_name']
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class MaterialsViewSet(generics.ListCreateAPIView):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    ordering_fields = ['material_author', 'material_name', 'material_code', 'material_color', 'material_quantity', 'material_location', 'material_hall', 'material_unit', 'material_date', 'is_active', 'is_available',]
    search_fields = ['material_code', 'material_name']
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class ProductsCardexViewSet(generics.ListCreateAPIView):
    queryset = ProductsCardex.objects.all()
    serializer_class = ProductsCardexSerializer
    ordering_fields = ['row', 'author', 'product', 'factor_number', 'number', 'description', 'operation', 'date', 'status', 'quantity']
    search_fields = ['product', 'factor_number',]
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class MaterialsCardexsViewSet(generics.ListCreateAPIView):
    queryset = MaterialsCardex.objects.all()
    serializer_class = MaterialsCardexsSerializer
    ordering_fields = ['row', 'author', 'material', 'factor_number', 'number', 'description', 'operation', 'date', 'status', 'quantity']
    search_fields = ['material', 'factor_number',]
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


''' Creare / update inventory '''
@login_required
@csrf_exempt
def js_add_products(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_code = request.POST.get('product_code')
        product_color = request.POST.get('product_color')
        product_location = request.POST.get('product_location')
        product_hall = request.POST.get('product_hall')
        product_unit = request.POST.get('product_unit')
        if product_name:
            if product_code:
                if product_color:
                    if product_location and product_location != "انتخاب محل انبار":
                        if product_hall and product_hall != "انتخاب سالن انبار":
                            if product_unit and product_unit != "انتخاب واحد شمارش":
                                if Products.objects.filter(product_name = product_name, product_code = product_code).exists():
                                    return JsonResponse({'status': 'محصول از قبل تعریف شده و موجود است', 'success': False})
                                else:
                                    full_name = request.user.first_name + " " + request.user.last_name
                                    Products.objects.create(
                                        product_author = full_name,
                                        product_name = product_name,
                                        product_code = product_code,
                                        product_color = product_color,
                                        product_quantity = 0,
                                        product_location = product_location,
                                        product_hall = product_hall,
                                        product_unit = product_unit,
                                    )
                                    return JsonResponse({'status': 'محصول با موفقیت افزوده شد', 'success':True})
                            else:
                                return JsonResponse({'status': 'واحد شمارش انتخاب نشده', 'success': False})
                        else:
                            return JsonResponse({'status': 'سالن انبار انتخاب نشده', 'success': False})
                    else:
                        return JsonResponse({'status': 'محل انبار انتخاب نشده', 'success': False})
                else:
                    return JsonResponse({'status': 'رنگ محصول را وارد کنید', 'success': False})
            else:
                return JsonResponse({'status': 'کد محصول را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status': 'نام محصول را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})

@login_required
@csrf_exempt
def js_add_materials(request):
    if request.method == 'POST':
        material_name = request.POST.get('material_name')
        material_code = request.POST.get('material_code')
        material_color = request.POST.get('material_color')
        material_location = request.POST.get('material_location')
        material_hall = request.POST.get('material_hall')
        material_unit = request.POST.get('material_unit')
        if material_name:
            if material_code:
                if material_color:
                    if material_location and material_location != "انتخاب محل انبار":
                        if material_hall and material_hall != "انتخاب سالن انبار":
                            if material_unit and material_unit != "انتخاب واحد شمارش":
                                if Materials.objects.filter(material_name = material_name, material_code = material_code).exists():
                                    return JsonResponse({'status': 'ماده اولیه از قبل تعریف شده و موجود است', 'success': False})
                                else:
                                    full_name = request.user.first_name + " " + request.user.last_name
                                    Materials.objects.create(
                                        material_author = full_name,
                                        material_name = material_name,
                                        material_code = material_code,
                                        material_color = material_color,
                                        material_quantity = 0,
                                        material_location = material_location,
                                        material_hall = material_hall,
                                        material_unit = material_unit,
                                    )
                                    return JsonResponse({'status': 'ماده اولیه با موفقیت افزوده شد', 'success':True})
                            else:
                                return JsonResponse({'status': 'واحد شمارش انتخاب نشده', 'success': False})
                        else:
                            return JsonResponse({'status': 'سالن انبار انتخاب نشده', 'success': False})
                    else:
                        return JsonResponse({'status': 'محل انبار انتخاب نشده', 'success': False})
                else:
                    return JsonResponse({'status': 'رنگ ماده اولیه را وارد کنید', 'success': False})
            else:
                return JsonResponse({'status': 'کد ماده اولیه را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status': 'نام ماده اولیه را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})

@login_required
@csrf_exempt
def js_update_products(request):
    if request.method == 'POST':
        factor_number = request.POST.get('factor_number')
        number = request.POST.get('number')
        description = request.POST.get('description')
        operation = request.POST.get('operation')
        product_code = request.POST.get('product_code')
        if factor_number:
            if number:
                if operation and operation != "انتخاب عملیات":
                    if description:
                        if product_code:
                            if Products.objects.filter(product_code = product_code).exists():
                                if ProductsCardex.objects.filter(product = product_code, factor_number = factor_number).exists():
                                    return JsonResponse({'status':'کادرکس با این شماره فاکتور هم اکنون تعریف شده', 'success': False})
                                else:
                                    full_name = request.user.first_name + " " + request.user.last_name
                                    product = Products.objects.filter(product_code = product_code).first()
                                    if operation == "ورودی":
                                        total = product.product_quantity + int(number)
                                        product.product_quantity = total
                                        product.save()
                                        ProductsCardex.objects.create(
                                            author = full_name,
                                            product = product_code,
                                            factor_number = factor_number,
                                            number = number,
                                            description = description,
                                            operation = operation,
                                            status = True,
                                            quantity = product.product_quantity,
                                        )
                                        return JsonResponse({'status': 'کاردکس با موفقیت ایجاد و موجودی به روز شد', 'success': True})
                                    elif operation == "خروجی":
                                        if product.product_quantity == 0:
                                            return JsonResponse({'status':'محصول مورد نظر فاقد موجودی است', 'success': False})
                                        else:
                                            total = product.product_quantity - int(number)
                                            product.product_quantity = total
                                            product.save()
                                            ProductsCardex.objects.create(
                                                author = full_name,
                                                product = product_code,
                                                factor_number = factor_number,
                                                number = number,
                                                description = description,
                                                operation = operation,
                                                status = False,
                                                quantity = product.product_quantity,
                                            )
                                            return JsonResponse({'status': 'کاردکس با موفقیت ایجاد شد و موجودی به روز شد', 'success': True})
                            else:
                                return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                        else:
                            return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                    else:
                        return JsonResponse({'status':'شرح عملیات را وارد کنید', 'success': False})
                else:
                    return JsonResponse({'status':'عملیات را انتخاب کنید', 'success': False})
            else:
                return JsonResponse({'status':'تعداد را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status':'شماره فاکتور را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})

@login_required
@csrf_exempt
def js_update_materials(request):
    if request.method == 'POST':
        factor_number = request.POST.get('factor_number')
        number = request.POST.get('number')
        description = request.POST.get('description')
        operation = request.POST.get('operation')
        material_code = request.POST.get('material_code')
        if factor_number:
            if number:
                if operation and operation != "انتخاب عملیات":
                    if description:
                        if material_code:
                            if Materials.objects.filter(material_code = material_code).exists():
                                if MaterialsCardex.objects.filter(material = material_code, factor_number = factor_number).exists():
                                    return JsonResponse({'status':'کادرکس با این شماره فاکتور هم اکنون تعریف شده', 'success': False})
                                else:
                                    full_name = request.user.first_name + " " + request.user.last_name
                                    material = Materials.objects.filter(material_code = material_code).first()
                                    if operation == "ورودی":
                                        total = material.material_quantity + int(number)
                                        material.material_quantity = total
                                        material.save()
                                        MaterialsCardex.objects.create(
                                            author = full_name,
                                            material = material_code,
                                            factor_number = factor_number,
                                            number = number,
                                            description = description,
                                            operation = operation,
                                            status = True,
                                            quantity = material.material_quantity,
                                        )
                                        return JsonResponse({'status': 'کاردکس با موفقیت ایجاد و موجودی به روز شد', 'success': True})
                                    elif operation == "خروجی":
                                        if material.material_quantity == 0:
                                            return JsonResponse({'status':'محصول مورد نظر فاقد موجودی است', 'success': False})
                                        else:
                                            total = material.material_quantity - int(number)
                                            material.material_quantity = total
                                            material.save()
                                            MaterialsCardex.objects.create(
                                                author = full_name,
                                                material = material_code,
                                                factor_number = factor_number,
                                                number = number,
                                                description = description,
                                                operation = operation,
                                                status = False,
                                                quantity = material.material_quantity,
                                            )
                                            return JsonResponse({'status': 'کاردکس با موفقیت ایجاد شد و موجودی به روز شد', 'success': True})
                            else:
                                return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                        else:
                            return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                    else:
                        return JsonResponse({'status':'شرح عملیات را وارد کنید', 'success': False})
                else:
                    return JsonResponse({'status':'عملیات را انتخاب کنید', 'success': False})
            else:
                return JsonResponse({'status':'تعداد را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status':'شماره فاکتور را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})

''' Render pages '''
@login_required
def materials(request):
    materials = Materials.objects.all().order_by('-material_date')
    return render(request, "inventory/materials/materials.html", {'materials' : materials})

@login_required
def add_materials(request):
    return render(request, "inventory/materials/add_materials.html")

@login_required
def products(request):
    products = Products.objects.all().order_by('-product_date')
    return render(request, "inventory/products/products.html", {'products' : products})

@login_required
def add_products(request):
    return render(request, "inventory/products/add_products.html")

@login_required
def add_products_cardex(request, code):
    product = Products.objects.filter(product_code = code)
    if product.exists():
        cardex = ProductsCardex.objects.filter(product = code).order_by('-date')
        context = {'code' : code, 'product' : product, 'cardex' : cardex}
        return render(request, "inventory/products/add_cardex.html", context)
    else:
        return render(request, "dashboard/dashboard.html")

@login_required
def add_materials_cardex(request, code):
    material = Materials.objects.filter(material_code = code)
    if material.exists():
        cardex = MaterialsCardex.objects.filter(material = code).order_by('-date')
        context = {'code' : code, 'material' : material, 'cardex' : cardex}
        return render(request, "inventory/materials/add_cardex.html", context)
    else:
        return render(request, "dashboard/dashboard.html")

@login_required
def inventory(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def product_cardex_export_to_excel(request, code):
    cardex = ProductsCardex.objects.filter(product = code).order_by("date")
    wb = Workbook()
    ws = wb.active
    ws.append(["ردیف", "تاریخ", "شماره حواله/فاکتور", "شرح اقدامات", "ورودی", "خروجی", "موجودی", "اقدام کننده",])
    for data in cardex:
        if data.status:
            ws.append([data.row, data.jpub(), data.factor_number, data.description, data.number, "0", data.quantity, data.author])
        else:
            ws.append([data.row, data.jpub(), data.factor_number, data.description, "0", data.number, data.quantity, data.author])
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=cardex-{code}.xlsx"
    wb.save(response)
    return response

@login_required
def material_cardex_export_to_excel(request, code):
    cardex = MaterialsCardex.objects.filter(material = code).order_by("date")
    wb = Workbook()
    ws = wb.active
    ws.append(["ردیف", "تاریخ", "شماره حواله/فاکتور", "شرح اقدامات", "ورودی", "خروجی", "موجودی", "اقدام کننده",])
    for data in cardex:
        if data.status:
            ws.append([data.row, data.jpub(), data.factor_number, data.description, data.number, "0", data.quantity, data.author])
        else:
            ws.append([data.row, data.jpub(), data.factor_number, data.description, "0", data.number, data.quantity, data.author])
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=cardex-{code}.xlsx"
    wb.save(response)
    return response

@login_required
def product_cardex_export_to_pdf(request, code):
    product = Products.objects.filter(product_code = code).order_by("product_date")
    if product.exists():
        cardex = ProductsCardex.objects.filter(product = code).order_by("date")
        context = {'code' : code, 'product': product, 'cardex': cardex}
        return render(request, "utils/print_product.html", context)
    else:
        return render(request, "dashboard/dashboard.html")

@login_required
def material_cardex_export_to_pdf(request, code):
    material = Materials.objects.filter(material_code = code).order_by("material_date")
    if material.exists():
        cardex = MaterialsCardex.objects.filter(material = code).order_by("date")
        context = {'code' : code, 'material': material, 'cardex': cardex}
        return render(request, "utils/print_material.html", context)
    else:
        return render(request, "dashboard/dashboard.html")
