from django.shortcuts import render
from .models import Blog

# Create your views here.
def listBlog(request):
    isiBlog = Blog.objects
    return render(request, 'blog/list-blog.html', {'blogs':isiBlog})

def detail(request):
    return render(request, 'blog/detail.html')