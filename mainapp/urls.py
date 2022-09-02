from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.index),
    path('results',views.results),
    path('base',views.base),
    path('temp',views.temp),
]