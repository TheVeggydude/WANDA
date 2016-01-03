from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'viewer/index.html')


def question(request):
    
    dict = {}
    
    if request.POST["root"] == "True":
        dict['answered'] = True
        dict['questionID'] = 0
    
        return render(request, 'viewer/question.html', dict)
    
    dict['answered'] = False
    
    return render(request, 'viewer/question.html', dict)


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