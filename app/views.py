from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}



    return render(request,'display_topic.html',context=d)
def webpage(request):
    
    web=Webpage.objects.all()
    web=Webpage.objects.filter(topic_name='football')
    web=Webpage.objects.exclude(topic_name='football')
    web=Webpage.objects.all()[3::]
    web=Webpage.objects.all()[::-1]
    web=Webpage.objects.all()
    web=Webpage.objects.all().order_by('name')
    web=Webpage.objects.all().order_by('-name')
    web=Webpage.objects.all().order_by(Length('topic_name'))


    


    
    s={'web':web}


    return render(request,'webpage.html',context=s)
