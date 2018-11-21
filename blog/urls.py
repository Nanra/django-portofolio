from django.urls import path
from . import views

urlpatterns = [

    path('', views.listBlog, name='listblog'),
]# Bagian untuk membari akses url ke media foto