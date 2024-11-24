from django.db import models

class Politician(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Image = models.ImageField(upload_to='politician_images/', null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.Name