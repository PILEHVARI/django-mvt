from django.shortcuts import render 
from .models import sevices

def home(request):
    #services = sevices.objects.all()
    services = sevices.objects.filter(status=True)
    return render(request,'root/index.html',context={'services':services})
def contact(request):
    return render(request,'root/contact.html')
def about(request):
    return render(request,'root/about.html')