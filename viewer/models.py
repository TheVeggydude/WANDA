from django.db import models

# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=400, default='answer')

class Question(models.Model):
    children = models.ForeignKey('self', blank=True, null=True, related_name='parent')
    answer = models.ForeignKey(Answer)
    text = models.CharField(max_length=200, default='question')
    
class Tree(models.Model):
    start = models.ForeignKey(Question)