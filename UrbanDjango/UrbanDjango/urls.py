"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import class_template,func_template
from task3.views import main_page,game_page,cart_page
from django.views.generic import TemplateView


urlpatterns = [
    path('', main_page),
    path('game_page/', game_page),
    path('cart_page/', cart_page),
    path('func_template/', func_template),
    path('class_template/', class_template.as_view()),
    # Второй вариант классового представления
    path('class_template2/', TemplateView.as_view(template_name='second_task/class_template.html'))
]
