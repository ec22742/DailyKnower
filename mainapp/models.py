from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import datetime
# Create your models here.


class topicTheme(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class dkTopic(models.Model):
    topicTheme = models.ForeignKey(topicTheme, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class adminPost(models.Model):
    topicTheme = models.ForeignKey(topicTheme, null=True, on_delete=models.SET_NULL)
    dkTopic = models.ForeignKey(dkTopic, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateField(('Date'), default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

    
    
class allReply(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(adminPost, on_delete=CASCADE, null=False)
    body = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__( self ):
        return self.body[0:60] 
    
