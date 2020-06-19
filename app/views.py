from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.


def topic(request):
    topics=Topic.objects.all()
    #topics=Topic.objects.filter(topic_name='Music')
    return render(request,'displaytopic.html',context={'topics':topics})


def webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(name='ronaldo')
    #webpages=Webpage.objects.order_by('url')
    #webpages=Webpage.objects.all()[0:5]
    #webpages=Webpage.objects.exclude(name='ronaldo')
    #webpages=Webpage.objects.filter(url__startswith='https')
    #webpages=Webpage.objects.filter(url__endswith='.com/')
    #webpages=Webpage.objects.filter(name__contains='Ro')
    #webpages=Webpage.objects.filter(Q(url__startswith='https'))
    #webpages=Webpage.objects.filter(Q(url__startswith='https') & Q(name__startswith='K'))
    #webpages=Webpage.objects.filter(Q(url__startswith='https') | Q(name__startswith='S'))
    #webpages=Webpage.objects.filter(Q(url__endswith='.com/') & Q(name__startswith='M'))


    return render(request,'displaywebpage.html',context={'webpages':webpages})



def access(request):
    #access=Access_Records.objects.all()
    access=Access_Records.objects.filter(date__gt='2011-03-12')
    #access=Access_Records.objects.filter(date__gte='2011-03-12')
    #access=Access_Records.objects.filter(date__lt='2011-03-12')
    #access=Access_Records.objects.filter(date__lte='2011-03-12')
    #access=Access_Records.objects.exclude(date__lte='2011-03-12')
    #access=Access_Records.objects.filter(date__year='2011')
    #access=Access_Records.objects.filter(date__month='03')
    #access=Access_Records.objects.filter(date__day='11')


    return render(request,'displayaccess.html',context={'access':access})

def deleteweb(request):
    #Webpage.objects.filter(name='Robert').delete()
    Webpage.objects.all().delete()

    webpages=Webpage.objects.all()

    #return HttpResponse('one record has been deleted successfully')
    return render(request,'displaywebpage.html',context={'webpages':webpages})


def updateweb(request):
    #Webpage.objects.filter(name='Dean').update(url='https://www.jones-garcia.biz/')
    #Webpage.objects.filter(name='Dean').update(name='Dhoni')
    Webpage.objects.filter(name='Dhoni').update(topic_name='Cricket')
    webpages=Webpage.objects.all()


    #return HttpResponse('one record as been updated')
    return render(request,'displaywebpage.html',context={'webpages':webpages})


def web_form(request):
    if request.method=='POST':
        #request.POST={'name':'value'}
        form_name=request.POST.get('name')#Katherine
        webpages=Webpage.objects.filter(name=form_name)
        return render(request,'displaywebpage.html',context={'webpages':webpages})


    return render(request,'web_form.html')

def create_topic(request):
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        t=Topic.objects.get_or_create(topic_name=topic_name)[0]
        t.save()
        #return HttpResponse('one topic has been added successfully')
        topics=Topic.objects.all()
        return render(request,'displaytopic.html',context={'topics':topics})
    return render(request,'create_topic.html')

def create_web(request):
    topics=Topic.objects.all()
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get('url')
        t=Topic.objects.get_or_create(topic_name=topic_name)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        #return HttpResponse('one record has been added')
        webpages=Webpage.objects.all()
        return render(request,'displaywebpage.html',context={'webpages':webpages})

    return render(request,'create_web.html',context={'topics':topics})

def select(request):
    topics=Topic.objects.all()
    return render(request,'select.html',context={'topics':topics})

def delete(request):
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        Topic.objects.filter(topic_name=topic_name).delete()
        topics=Topic.objects.all()
        return render(request,'displaytopic.html',context={'topics':topics})




