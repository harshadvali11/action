"""project12 URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topic/',views.topic,name='topic'),
    path('webpage/',views.webpage,name='webpage'),
    path('access/',views.access,name='access'),
    path('deleteweb/',views.deleteweb,name='deleteweb'),
    path('updateweb/',views.updateweb,name='updateweb'),
    path('web_form/',views.web_form,name='web_form'),
    path('create_topic/',views.create_topic,name='create_topic'),
    path('create_web/',views.create_web,name='create_web'),
    path('select/',views.select,name='select'),
    path('delete/',views.delete,name='delete'),







    
    
]
