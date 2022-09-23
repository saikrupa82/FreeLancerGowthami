from django.shortcuts import render
from .models import *
from django.core import serializers
import json
from new_gowthami.settings import  MEDIA_URL,MEDIA_ROOT

# Create your views here.

def index(request):
    # def get_ip(request):
    #     address = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if address:
    #         ip=address.split(',')[-1].strip()
    #     else:
    #         ip=request.META.get('REMOTE_ADDR')
    #     return ip
    # ip_=get_ip(request)
    # user=ipModel(ip=ip_)
 
    # user.save()
    # count=ipModel.objects.all().count()
    # candidates = Selected_candidate_list.objects.all()

    announcement = Announcement.objects.all().order_by('-UID')[:3]
    notification = Notification.objects.all().order_by('-UID')[:3]
    Selected_candidate ={'Inter':300,'Navy':220,'Air force':250,'Army':320,'NDA':150,'State Police':220}
    # Slider_Img = Slider_home_page_left_top.objects.all()
    # Testimonial = testimonial_home_page.objects.all()
    context = {
        'announcement':announcement,
        'notification':notification,
        # 'Visitor_Count':count,
        # 'Slider_Img':Slider_Img,
        # 'testimonial': Testimonial,
        # 'candidates':candidates,
    }
    # context.update(context_global)
    context.update(Selected_candidate)
    return render(request, 'index.html',context)

def results(request):    

    def get_json(obj):
        json_text = [str(obj.Slider_Img),obj.Name_Student,obj.SelectedIN,'{}'.format(obj.Year.year)]
        return json_text

    
    # Defence    
    temp=[]
    result_defence_main = Results.objects.filter(Field_Student='Defence',Image_Student='1')[0]
    temp.append(get_json(result_defence_main))
    result_defence = Results.objects.filter(Field_Student='Defence').exclude(id = str(result_defence_main.id))

    for i in result_defence:
        temp.append(get_json(i))
    print(temp)
    def_imgs = json.dumps(temp)
    print(def_imgs)

    # Inter
    temp=[]
    result_Inter_main = Results.objects.filter(Field_Student='Inter',Image_Student='1')[0]
    temp.append(get_json(result_Inter_main))

    result_Inter = Results.objects.filter(Field_Student='Inter' ).exclude(id = str(result_Inter_main.id))
    for i in result_Inter:
        temp.append(get_json(i))
    inter_imgs = json.dumps(temp)
    print(inter_imgs)

    context = {
        'inter_imgs' : inter_imgs,
        'def_imgs': def_imgs,
        'MEDIA_URL':MEDIA_URL,
        'MEDIA_ROOT':MEDIA_ROOT,
    }
    return render(request, 'results.html',context)


def notification(request):
    

    def get_json(obj):
        json_text = [obj.Text,'{}-{}-{}'.format(obj.from_date.day,obj.from_date.month,obj.from_date.year),'{}-{}-{}'.format(obj.end_date.day,obj.end_date.month,obj.end_date.year),obj.link]
        print(obj.link)
        return json_text
    notice_army = Notification.objects.filter(SubCategory='army')
    lst=[]
    notis={}
    
    for i in notice_army:
        
        lst.append(get_json(i))
        
    notis["army"] = lst
    
    notice_navy = Notification.objects.filter(SubCategory='navy')
    lst=[]
    for i in notice_navy:
        
        lst.append(get_json(i))
        {'navy':lst}
    notis["navy"] = lst

    notice_airforce = Notification.objects.filter(SubCategory='airforce')
    lst_=[]
    for i in notice_airforce:
        lst.append(get_json(i))
        {'airforce':lst}
    notis["airforce"] = lst

    notice_paramilitary = Notification.objects.filter(SubCategory='paramilitary')
    lst_=[]
    for i in notice_paramilitary:
        lst.append(get_json(i))
        {'paramilitary':lst}
    notis["paramilitary"] = lst


    notice_other= Notification.objects.filter(SubCategory='other')
    lst_=[]
    for i in notice_other:
        lst.append(get_json(i))
        {'other':lst}
    notis["other"] = lst
    notis = json.dumps(notis)
    context = {
        'sub_category' : 1,
        'title': 'Notification',
        'notis':notis,
    }
    return render(request, 'notification.html', context)

def carrers(request):
    
    carrer = Carrer.objects.all()
    
   
    context = {
        'sub_category' : 0,
        'title': 'Carrers',
        'list': carrer,
    }
    return render(request, 'notification.html', context)

def announcement(request):
    
    announcement = Announcement.objects.all()
    
   
    context = {
        'sub_category' : 0,
        'announcement_tab': 1,
        'title': 'Announcement',
        'list': announcement,
    }
    return render(request, 'notification.html', context)

def document(request):
    context = {
        'title': 'Model Papers',
    }
    return render(request, 'documents.html' , context)

def syllabus(request):
    context = {
        'title':' Syllabus',
    }
    return render(request, 'documents.html', context)

def brochure(request):
    context = {
        'title': 'Brochure',
    }
    return render(request, 'documents.html',context)

def enquiry(request):
    context = {
    }
    return render(request, 'enquiry.html',context)

def base(request):
    return render(request, 'base.html')
    
def media(request):
    return render(request, 'media.html')

def gallery(request):
    return render(request, 'gallery.html')

def courses(request):
    return render(request, 'courses.html')

def temp(request):
    return render(request, 'temp.html')