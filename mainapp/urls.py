from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.index),
    path('results',views.results,name="results"),
    path('base',views.base),
    path('temp',views.temp),
    path('notification',views.notification,name="notification"),
    path('announcement',views.announcement,name="announcement"),
    path('document',views.document,name="document"),
    path('syllabus',views.syllabus,name="syllabus"),
    path('brochure',views.brochure,name="brochure"),
    path('carrers',views.carrers,name="carrers"),
    path('enquiry',views.enquiry),
    
]