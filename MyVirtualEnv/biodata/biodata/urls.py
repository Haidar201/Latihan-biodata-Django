"""biodata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyBio.views import home_view, create_view, extra_create,read_view,update_view,isi_view,update_isi_view,delete_view,pos_delete_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home', home_view, name='home'),
    path('read/', read_view, name='read'),
    path('read/<str:pk>/', isi_view, name = 'isi'),
    path('update/<str:pk>/', update_isi_view, name = 'confirm_update'),
    path('delete/<str:pk>/', pos_delete_view, name = 'confirm_delete'),
    path('delete/', delete_view, name='delete'),
    path('update/', update_view, name='update'),
    path('create/', create_view, name='create'),
    path('extra/<int:num1>/<int:num2>/', extra_create, name='extra')
]
