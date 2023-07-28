from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Questions(models.Model):
    content = models.CharField(max_length=500)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    Note = models.CharField(max_length=500)

class Answers(models.Model):
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2)