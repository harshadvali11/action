#we have to create django environment
import os

#os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project_name.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project12.settings')

#we need access the features of django
import django

django.setup()

#from here actual population starts
from app.models import *

from faker import Faker
f=Faker()
import random
topics=['Sports','Music','Dance','Singing']

def Add_topics():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def Add_webpage(webpagename,url):
    topic_name=Add_topics()#Music
    w=Webpage.objects.get_or_create(topic_name=topic_name,name=webpagename,url=url)[0]
    w.save()
    return w


def Add_records(webpagename,url,date):
    name=Add_webpage(webpagename,url)
    a=Access_Records.objects.get_or_create(name=name,date=date)[0]
    a.save()
    return a

n=int(input('enter how data u need to insert'))

def Add_data(n):
    for i in range(n):
        f_name=f.first_name()
        f_url=f.url()
        f_date=f.date()

        Add_records(f_name,f_url,f_date)

if __name__=='__main__':
    print('now we have started populating')
    Add_data(n)
    print('populating of data is done successfully')


#python filename.py










