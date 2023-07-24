from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse


# Create your views here.

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")    
    return render(request, 'polls/detail.html',{'question':question})

# def result(request, question_id):    
#     response = "you're looking at the results of question %s."
#     return HttpResponse(response % question_id)
def result(request, question_id):    
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    # print(f"resquen.polls.choine : {request.POST['choice']}")

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render (request, 'polls/detail.html',{
            'question': question,
            'error_messsage' :" You didn't select a choice"
                    })
    else:
        selected_choice.votes +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
