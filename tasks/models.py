from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    title = models.CharField(max_length=225) # Title of the task

    pub_date = models.DateTimeField() # Task publishing date

    details = models.TextField(blank=True) # Details about the task

    task_date = models.DateField(auto_now=False,blank=True,null=True)

    task_time = models.TimeField(auto_now=False,blank=True,null=True)

    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)


    def summary(self):
        return self.details[:100]


    def __str__(self):
        return self.title
