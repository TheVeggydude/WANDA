from django.db import models


# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=400, default='Please update this answer text.')

class Question(models.Model):
    children = models.ForeignKey('self', blank=True, null=True, related_name='parent')
    answers = models.ForeignKey(Answer, null=True)
    text = models.CharField(max_length=400, default='Please update this question text.')
    
class Tree(models.Model):
    start = models.ForeignKey(Question)

'''
class Answer(models.Model):
    text = models.CharField(max_length=400, default='answer')
    next = models.ForeignKey(Question)

class Question(models.Model):
    answers = models.ForeignKey(Answer)
    text = models.CharField(max_length=200, default='question')
    
class Tree(models.Model):
    start = models.ForeignKey(Question)
'''