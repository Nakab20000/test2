from django.db import models

# Create your models here.
class subject(models.Model):
    Course_id = models.CharField(max_length=110,primary_key=True)
    Course_name = models.CharField(max_length=100)
    Teacher_name = models.CharField(max_length=100)