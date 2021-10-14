from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
from .models import Question

# def index(request):
# 	# return HttpResponse("Hello, world. You're at the poll index.")
# 	question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	# output = ', '.join([q.question_text for q in question_list])
# 	context = {
# 		'question_list': question_list,
# 	}
# 	return HttpResponse(template.render(context, request))

# Using shortcut to render template using render()
def index(request):
	question_list = Question.objects.order_by('-pub_date')[:5]
	context = { 'question_list': question_list }
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s. " % question_id)

def results(request, question_id):
	response = "You're looking at the results of the question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)