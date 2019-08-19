from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=225)

    pub_date = models.DateTimeField()

    details = models.TextField()

    task_date = models.DateField(auto_now=False,blank=True,null=True)

    task_time = models.TimeField(auto_now=False,blank=True,null=True)

    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def prettydate(self):
        try:
            return self.task_time.strftime(' %b %e %Y')

        except:
            pass

    def summary(self):
        return self.details[:100]


    def __str__(self):
        return self.title
