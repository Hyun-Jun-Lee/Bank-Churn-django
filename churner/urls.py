from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "churner"

urlpatterns = [    
    path('', views.index, name ="index_page"),
    path('predict/', views.predict, name ="predict"),
    path('results/', views.view_results, name='result'),
]