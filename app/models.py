from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return self.topic_name



class Webpage(models.Model):
    #attributename=models.ForeignKey(to whichtable,on_delete=models.CASCADE)
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    url=models.URLField(max_length=40)

    def __str__(self):
        return self.name



class Access_Records(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return self.date

#auto_now=True
 #model created on 10 june
 #inserting on 24 june
 #date=24 june
 #insert on 31 dec
 #date=31 dec


#auto_now_add
     #model created on 10 june
     #inserting on 24 june
     #date=10 june

     #insert data on 31 dec
     #date=10 june











