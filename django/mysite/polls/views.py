from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Question, Choice


#def index(request):
#    """ Display the root page to of the URL .../polls/
#    :param request:
#    :return HttpResponse :
#    """
#    latest_question_list = Question.objects.order_by('-publication_date')[:5]

    # from django.template import RequestContext
    # from django.template import loader

    # template = loader.get_template('polls/index.html')
    # context_instance = RequestContext(request, {
    #     'latest_question_list' : latest_question_list,
    # })
    #output = '| '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(template.render(context_instance))

#    context_params = { 'latest_question_list' : latest_question_list }
#    return render(request, 'polls/index.html', context_params)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        :return: the last five published questions.
        """
        return Question.objects.order_by('-publication_date')[:5]

'''
def detail(request, question_id):
    """ Display the detail of a particular question.
    :param request: HttpRequest
    :param question_id: Integer
    :return HttpResponse:
    """
    # return HttpResponse("You're looking at question, id=%s." % question_id)
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist!!")
#    return render(request, 'polls/detail.html', {'question' : question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})
'''

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    """ Handle the vote request.

    :param request:
    :param question_id:
    :return HttpResponse:
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
