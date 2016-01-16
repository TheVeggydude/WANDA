from django.shortcuts import render
from viewer.models import *


# Simple, just return the standard home page of the site.
def index(request):
    return render(request, 'viewer/index.html')

# Either returns a page with a question and answers or a page showing the final result arrived at.
def question(request):
    
    # Create an empty context dictionary used for transferring data to the template engine.
    context = {}

    # If start, then select the first question in the tree to be shown.
    if 'start' in request.POST:
        context['question'] = Tree.objects.all().first().start
    
        return render(request, 'viewer/question.html', context)

    # Not a start node, so get the answer text and find the corresponding question.
    question = Question.objects.all().get(id = request.POST['question'])

    # This piece of code finds the child node that corresponds with the chosen answer.
    counter = 0
    for answer in question.answer_set.all():
        counter +=1
        if answer.text == request.POST['choice']:
            break

    child = None
    for current_child in question.children.all():
        counter-=1
        if counter==0:
            child = context['question'] = current_child
            break

    # If child has no children, you must be at a leaf node and a result so show the correct page for it.
    if not child.children.all().exists():
        return render(request, 'viewer/result.html', context)
    
    # Else just render the normal question page.
    return render(request, 'viewer/question.html', context)


# Error Responses:
# Special functions Django uses to call error pages automatically when needed.

def handler404(request):
    return render(request,
                      'viewer/404.html')


def handler502(request):
    return render(request,
                      'viewer/502.html')


def handler500(request):
    return render(request,
                      'viewer/500.html')