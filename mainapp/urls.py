from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('results',views.results,name="results"),
    path('base',views.base),
    path('temp',views.temp),
    path('notification',views.notification,name="notification"),
    path('announcement',views.announcement,name="announcement"),
    path('document',views.document,name="document"),
    path('syllabus',views.syllabus,name="syllabus"),
    path('brochure',views.brochure,name="brochure"),
    path('Carrers',views.carrers,name="carrers"),
    path('enquiry',views.enquiry),
    path('media',views.media,name="media"),
    path('gallery',views.gallery,name="gallery"),
    path('Courses',views.selected_courses,name="courses"),
    path('Courses/Inter',views.selected_courses_Inter,name="coursesInter"),
    path('Courses/Army',views.selected_courses_Army,name="coursesArmy"),
    path('Courses/Navy',views.selected_courses_Navy,name="coursessNavy"),
    path('Courses/Air Force',views.selected_courses_AirForce,name="coursesAirForce"),
    path('Courses/NDA',views.selected_courses_NDA,name="coursesNDA"),
    path('Courses/State Police',views.selected_courses_StatePolice,name="coursesStatePolice"),
    path('Courses/Paramilitary Forces',views.selected_courses_ParamilitaryForces,name="coursesParamilitaryForces"),

]