from django import forms
from .models import Customer, Technician, ServiceRequest

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['name', 'contact', 'skills']

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['title', 'description', 'status', 'priority', 'assigned_technician', 'customer']
