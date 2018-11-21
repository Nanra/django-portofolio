from django.urls import path
from . import views

urlpatterns = [

    path('', views.listBlog, name='listblog'),
    path('<int:blog_id>', views.detail, name='detail'),
]# Bagian untuk membari akses url ke media foto