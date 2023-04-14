"""midMorningCatTwo URL Configuration

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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_register, name='employee-reg'),
    path('about/', views.about, name='site-about'),
    path('blog/', views.blog, name='site-blog'),
    path('client/', views.client, name='site-client'),
    path('contact/', views.contact, name='site-contact'),
    path('index/', views.index, name='site-home'),
    path('services/', views.services, name='site-services'),
    path('employee/', views.employee_hr, name='site-employee'),

]
