from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:5]
    output = '| '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    """
    :param request: HttpRequest
    :param question_id: Integer
    :return: 
    """
    return HttpResponse("You're looking at question, id=%s." % question_id)


def results(request, question_id):
    """
    :param request: ditto
    :param question_id: ditto
    :return:
    """
    response = "You're looking at the results of question id=%s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """

    :param request:
    :param question_id:
    :return:
    """
    return HttpResponse("You're voting on question, id=%s" % question_id)