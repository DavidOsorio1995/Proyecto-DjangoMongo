from django.urls import path
from inventory_app import views

urlpatterns = [
    path('', views.compra, name='compra'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('categories/create/', views.category_create, name='category_create'),
    path('providers/create/', views.provider_create, name='provider_create'),
    path('compra/', views.compra, name='compra'),
    path('agregar_al_carrito/<int:pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('realizar_compra/', views.realizar_compra, name='realizar_compra'),
    path('compra_confirmada/', views.compra_confirmada, name='compra_confirmada'),
    path('quitar_del_carrito/<int:pk>/', views.quitar_del_carrito, name='quitar_del_carrito'),
     path('login/', views.login, name='login'),
]
