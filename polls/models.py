import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth import get_user_model

days = 365

# Create your models here.
#class Question(models.Model):
#   question_text = models.CharField(max_length=200)
#   pub_date = models.DateTimeField('date published')
#   def __str__(self):
#      return self.question_text
#   @admin.display(
#      boolean=True,
#      ordering="pub_date",
#      description="Published within " + str(days) + " days?",
#   )
#   def was_published_recently(self):
#      now = timezone.now()
#      return now - datetime.timedelta(days) <= self.pub_date <= now
#
#class Choice(models.Model):
#   question = models.ForeignKey(Question, on_delete=models.CASCADE)
#   choice_text = models.CharField(max_length=200)
#   votes = models.IntegerField(default=0)
#   def __str__(self):
#        return self.choice_text
   
class Election(models.Model):
   election = models.CharField(max_length=100)
   pub_date = models.DateTimeField('date published')
   def __str__(self):
      return self.election
   @admin.display(
      boolean=True,
      ordering="pub_date",
      description="Published within " + str(days) + " days?",
   )
   def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days) <= self.pub_date <= now
   
class Vote(models.Model):
   user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
   election = models.ForeignKey(Election, on_delete=models.CASCADE)
   vote = models.IntegerField(default=0)
   pub_date = models.DateTimeField('date published')
   def __str__(self):
      user = str(self.user_name)
      return user
   @admin.display(
     boolean=True,
     ordering="pub_date",
     description="Published within " + str(days) + " days?",
   )
   def was_published_recently(self):
     now = timezone.now()
     return now - datetime.timedelta(days) <= self.pub_date <= now