from django.urls import path
from .views import (index, product, add_product, save_product, delete_product, reports_product,
                    form_update_product, update_product)

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('add-product/', add_product, name='add-product'),
    path('reports-product/', reports_product, name='reports-product'),

    #proses simpan kedatabase pada model product
    path('save_product/', save_product, name='save_product'),
    
    #delete data eproduct
    path('delete_product/<int:id>', delete_product, name='delete_product'),

    #edit data product
    path('form_update_product/<int:id>', form_update_product, name='form_update_product'),

    #untuk update product
    path('update_product/<int:id>', update_product, name='update_product'),
]
