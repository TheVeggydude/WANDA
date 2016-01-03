from django.db import models

# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=400, default='answer')

class Node(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    answer = models.ForeignKey(Answer)
    question_text = models.CharField(max_length=200, default='question')
    result = models.BooleanField(default=False)