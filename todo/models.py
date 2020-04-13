from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100) #max length is 100 letters
    memo = models.TextField(blank=True) #can fill in empty
    datecreated = models.DateTimeField(auto_now_add=True) #show when it was created
    datecompleted = models.DateTimeField(null=True) #when it was finished
    importance = models.BooleanField(default=False) #checkbox  importance of todo
    user = models.ForeignKey(User, on_delete=models.CASCADE) #stores relationship with user(user id)



