from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def listBlog(request):
    isiBlog = Blog.objects
    return render(request, 'blog/list-blog.html', {'blogs':isiBlog})

def detail(request, blog_id):
    detailBlog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'isiDetail':detailBlog})