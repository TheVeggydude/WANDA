from django.shortcuts import render
from viewer.models import *


# Create your views here.
def index(request):
    return render(request, 'viewer/index.html')


def question(request):
    
    context = {}

    # If start, then select the first question in the tree to be shown
    if 'start' in request.POST:
        context['question'] = Tree.objects.all().first().start
    
        return render(request, 'viewer/question.html', context)

    # Not a start node, so get the answer text and find the corresponding question
    print(request.POST['choice'])
    question = Answer.objects.get(text = request.POST['choice']).question
    counter = 0
    for answer in question.answer_set.all():
        counter +=1
        if answer.text == request.POST['choice']:
            break

    print(counter)
    for child in question.children.all():
        counter-=1
        if counter==0:
            context['question'] = child


    return render(request, 'viewer/question.html', context)


#Error Responses:


def handler404(request):
    return render(request,
                      'viewer/404.html')


def handler502(request):
    return render(request,
                      'viewer/502.html')


def handler500(request):
    return render(request,
                      'viewer/500.html')