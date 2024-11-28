import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

from polls.models import Election

days = 365

class Politician(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Image = models.ImageField(upload_to='politician_images/', null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.Name
    @admin.display(
      boolean=True,
      ordering="pub_date",
      description="Published within " + str(days) + " days?",
    )
    def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days) <= self.pub_date <= now
    
# class Result(models.Model):
#     politician = models.ForeignKey(Politician, on_delete=models.CASCADE)
#     votes = models.IntegerField(default=0)
#     pub_date = models.DateTimeField('date published')
#     
#     def __str__(self):
#         politician = str(self.politician)
#         return politician
#     @admin.display(
#       boolean=True,
#       ordering="pub_date",
#       description="Published within " + str(days) + " days?",
#     )
#     def was_published_recently(self):
#       now = timezone.now()
#       return now - datetime.timedelta(days) <= self.pub_date <= now