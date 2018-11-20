from django.contrib import admin
from .models import Job # Import Model yang mau di daftarkan di laman admin

# Register your models here.
admin.site.register(Job) # Mendaftarkan class Job dari Models