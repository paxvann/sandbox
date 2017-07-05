from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404

from django.template import RequestContext
from django.template import loader

from polls.models import Question, Choice


def index(request):
    """ Display the root page to of the URL .../polls/
    :param request:
    :return:
    """
    latest_question_list = Question.objects.order_by('-publication_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context_instance = RequestContext(request, {
    #     'latest_question_list' : latest_question_list,
    # })
    #output = '| '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(template.render(context_instance))
    context_params = { 'latest_question_list' : latest_question_list }
    return render(request, 'polls/index.html', context_params)


def detail(request, question_id):
    """ Display the detail of a particular question.
    :param request: HttpRequest
    :param question_id: Integer
    :return: 
    """
    # return HttpResponse("You're looking at question, id=%s." % question_id)
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist!!")
#    return render(request, 'polls/detail.html', {'question' : question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    """
    :param request: ditto
    :param question_id: ditto
    :return:
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question} )

def vote(request, question_id):
    """ Handle the vote request.

    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            'polls/detail.html',
            {'question':question,
             'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being
        # posted twice if a user hits the Back button.
        # Redirect to the 'result' page.
        return HttpResponseRedirect(reverse( 'polls_ns:results_url', args=(question.id,) ))
#        return HttpResponseRedirect(reverse( 'polls:results', args=(request.POST['csrfmiddlewaretoken'],) ))
