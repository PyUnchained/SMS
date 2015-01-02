from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150,blank=True)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    date = models.DateTimeField()
    creator = models.ForeignKey(User, blank=True, null = True)
    remind = models.BooleanField(default = False, blank = True)
    
    
    
    def __unicode__(self):
        if self.title:
            return unicode(self.creator) + u"-" + self.title
        else:
            return unicode(self.creator) + u"-" + self.snippet[:40]
        
    def short(self):
        if self.snippet:
            return "<i> %s</i>-  %s" %(self.title,self.snippet)
        else:
            return self.title
        short.allow_tags = True
        
    class Meta:
        verbose_name_plural = "entries"
    
    class Admin:
        pass

class Reminder(models.Model):
    time = models.DateTimeField()
    message = models.CharField(max_length = 500, blank = True)
    entries = models.ManyToManyField(Entry)

admin.site.register(Entry)
