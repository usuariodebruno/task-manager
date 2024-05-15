from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.user.username

class Task(models.Model):
    title = models.CharField(max_length=225, null=False)
    description = models.CharField(max_length=1225, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

