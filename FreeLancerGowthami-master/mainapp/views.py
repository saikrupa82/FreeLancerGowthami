from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def results(request):
    return render(request, 'results.html')

def notification(request):
    context = {
        'sub_category' : 1,
        'title': 'Notification',
    }
    return render(request, 'notification.html', context)

def carrers(request):
    context = {
        'sub_category' : 0,
        'title': 'Carrers',
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
    
def temp(request):
    return render(request, 'temp.html')