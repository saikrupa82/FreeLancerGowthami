from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.index),
    path('results',views.results,name="results"),
    path('base',views.base),
    path('temp',views.temp),
    path('notification',views.notification),
    path('document',views.document),
    path('syllabus',views.syllabus),
    path('brochure',views.brochure),
    path('carrers',views.carrers),
    path('enquiry',views.enquiry),
    
]