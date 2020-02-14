"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
 
from myapp.views import home_view,next_view,form_view,raw_html_form_view,raw_form_view,get_data,get_data_one

urlpatterns = [
    path('', home_view, name='home'),
    path('next/', next_view, name='next'), #paths
    path('admin/', admin.site.urls),
    path('form/', form_view, name='form'),
    path('rawForm/', raw_form_view, name='rawForm'),
    path('rawHtmlForm/', raw_html_form_view, name='rawHtmlForm'),
    path('getForm/', get_data, name='getForm'),
    path('getForm/<int:id>/', get_data_one, name='getFormOne')
]
