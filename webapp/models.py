from django.db import models

# Create your models here.

class UserInput(models.Model):
    cUserName = models.CharField(max_length=255, null=False, default='')
    cUserAccount = models.CharField(max_length=255, null=False, default='')
    cUserPassword = models.CharField(max_length=255, null=False, default='')
    cUserPicture = models.CharField(max_length=255, blank=True, default='')
    cUserStyle = models.CharField(max_length=255, blank=True, default='w')
    cUserScore = models.CharField(max_length=255, blank=True, default='0')
    cUserStuff = models.CharField(max_length=255, blank=True, default='')
    cUserTemporarilyScore = models.CharField(max_length=255, blank=True, default='0')
    
    def __str__(self):
        return self.cUserAccount