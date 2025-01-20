from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'), 
    path('service-requests/', views.service_request_list, name='service_request_list'),
    path('service-request/create/', views.service_request_create, name='service_request_create'),
    path('service-request/<int:pk>/update/', views.service_request_update, name='service_request_update'),
    path('service-request/<int:pk>/delete/', views.service_request_delete, name='service_request_delete'),
    
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_create, name='customer_create'),
    path('customer/<int:pk>/update/', views.customer_update, name='customer_update'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    
    path('technicians/', views.technician_list, name='technician_list'),
    path('technician/create/', views.technician_create, name='technician_create'),
    path('technician/<int:pk>/update/', views.technician_update, name='technician_update'),
    path('technician/<int:pk>/delete/', views.technician_delete, name='technician_delete'),


]
