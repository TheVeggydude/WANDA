from django.db import models


# Create your models here.
class Question(models.Model):
    children = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='parents')
    text = models.CharField(max_length=400, default='Please update this question text.')


class Answer(models.Model):
    text = models.CharField(max_length=400, default='Please update this answer text.')
    question = models.ForeignKey(Question, null=True)

    
class Tree(models.Model):
    start = models.ForeignKey(Question)