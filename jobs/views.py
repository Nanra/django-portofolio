from django.shortcuts import render
from .models import Job # Memanggil Model Job pada database

# Create your views here.
def home(request):
    isiJobs = Job.objects # Memanggil semua isi dari model Job pada database
    return render(request, 'jobs/home.html', {'jobs': isiJobs})
