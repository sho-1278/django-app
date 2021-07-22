from django.contrib import admin
from django.urls import path, include
from resf.views import *

urlpatterns = [
    path('index', index, name='index'),
    path('greet', greet, name='thank_you_page')
]