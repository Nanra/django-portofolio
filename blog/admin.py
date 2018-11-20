from django.contrib import admin
from .models import Blog # Import Model yang mau di daftarkan di laman admin

# Register your models here.
admin.site.register(Blog) # Mendaftarkan class Blog dari Models