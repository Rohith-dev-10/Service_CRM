from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Technician, ServiceRequest
from .forms import CustomerForm, TechnicianForm, ServiceRequestForm

# List all service requests
def service_request_list(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'service_request_list.html', {'service_requests': service_requests})

# Create a new service request
def service_request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_request_form.html', {'form': form})

# Update an existing service request
def service_request_update(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'service_request_form.html', {'form': form})

# Delete a service request
def service_request_delete(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        service_request.delete()
        return redirect('service_request_list')
    return render(request, 'service_request_confirm_delete.html', {'service_request': service_request})

# List all customers
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

# Create a new customer
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

# List all technicians
def technician_list(request):
    technicians = Technician.objects.all()
    return render(request, 'technician_list.html', {'technicians': technicians})

# Create a new technician
def technician_create(request):
    if request.method == 'POST':
        form = TechnicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('technician_list')
    else:
        form = TechnicianForm()
    return render(request, 'technician_form.html', {'form': form})

def home(request):
    return redirect('service_request_list')  # Redirecting to service requests list or any other page

# Update an existing Technician
def technician_update(request, pk):
    technician = get_object_or_404(Technician, pk=pk)
    if request.method == 'POST':
        form = TechnicianForm(request.POST, instance=technician)
        if form.is_valid():
            form.save()
            return redirect('technician_list')
    else:
        form = TechnicianForm(instance=technician)
    return render(request, 'technician_form.html', {'form': form})

# Delete a Technician
def technician_delete(request, pk):
    technician = get_object_or_404(Technician, pk=pk)
    if request.method == 'POST':
        technician.delete()
        return redirect('technician_list')
    return render(request, 'technician_confirm_delete.html', {'technician': technician})

from .models import Customer
from .forms import CustomerForm

# Update an existing Customer
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})

# Delete a Customer
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})
