
# Register your models here.
from django.contrib import admin
from .models import Customer, Technician, ServiceRequest

# Register your models here.
admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(ServiceRequest)
