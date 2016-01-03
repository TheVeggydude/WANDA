from django.shortcuts import render
from viewer.models import *


# Create your views here.
def index(request):
    return render(request, 'viewer/index.html')


def question(request):
    
    context = {}

    # If root, then select the first question in the tree to be shown
    if 'start' in request.POST:
        context['question'] = Tree.objects.all().first().start
    
        return render(request, 'viewer/question.html', context)
    
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