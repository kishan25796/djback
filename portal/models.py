from django.db import models

# Create your models here.
class Homework(models.Model):
    stu_id = models.IntegerField()
    homework_json = models.JSONField()
    last_date = models.DateField()
    batch = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    
    def __str__(self):
        return self.stu_id
      


