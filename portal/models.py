from django.db import models

# Client/User model (for login functionality)
class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)  
    password = models.CharField(max_length=255)


class Performance(models.Model):
    performanceID = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255, default='default_image.jpg') 

class Stall(models.Model):
    stallID = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255, default='default_image.jpg') 

class Activity(models.Model):
    activityID = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255, default='default_image.jpg') 

class StarredItem(models.Model):
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)  #performance/activity/stall
    object_id = models.CharField(max_length=255)  

class Meta:
        unique_together = ('clientID', 'content_type', 'object_id') #supaya user blh star item sekali ja

class Feedback(models.Model):
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE) 
    username = models.CharField(max_length=100) 
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



