from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('dashboard/add/', views.add_product, name='add_product'),
]