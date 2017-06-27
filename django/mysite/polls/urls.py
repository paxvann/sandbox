from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    # e.g. /polls/
    url(r'^$', views.index, name='index'),
    # e.g. /polls/5
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # e.g. /polls/5/results
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # e.g. /polls/5/results
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

)