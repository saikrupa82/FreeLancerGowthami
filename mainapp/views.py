from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def results(request):
    return render(request, 'results.html')

def notification(request):
    return render(request, 'notification.html')

def base(request):
    return render(request, 'base.html')
def temp(request):
    return render(request, 'temp.html')