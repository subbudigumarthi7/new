"""Hpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include

from happx import views
app_name='happx'

urlpatterns = [
    url('admin/', admin.site.urls),
    url('happx/',include('happx.urls')),
    url(r'^base/',views.base,name='base'),
    url(r'^register/',views.register,name='register'),
    url(r'^auth_login/',views.auth_login,name='auth_login'),
    url(r'^index/',views.index,name='index'),
    url(r'^about/',views.about,name='about'),
    url(r'^pro/', views.pro, name='pro'),
    url(r'^smart/', views.smart, name='smart'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^submit/', views.submit, name='submit'),
]
