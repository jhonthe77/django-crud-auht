from django.db import models
from django.contrib.auth.models import User

class tasks (models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField(max_length=300)
    created_at= models.DateTimeField(auto_now_add=True)
    datecompleted= models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user= models.ForeignKey( User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
