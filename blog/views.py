from django.shortcuts import render

# Create your views here.
def listBlog(request):
    return render(request, 'blog/list-blog.html')