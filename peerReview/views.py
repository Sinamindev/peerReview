#import os
#import requests
from django.shortcuts import render
from django.http import HttpResponse

from .utils import html_table, assignPeers

from .models import Greeting



# Create your views here.
def index(request):
	#hreturn HttpResponse('Hello from Python!')
	#return render(request, 'index.html')
	return render(request, 'form.html')

def search(request):
	if request.method == 'POST':
		assignments = []
		X = int(request.POST.get('peers', None))
		Y = int(request.POST.get('reviews', None))
		try:
			assignments = assignPeers(X,Y)
			#html = html_table(assignments)
			#template = loader.get_template('display_names.html')
			#html = ', '.join([assignments for q in assignments])
			context = {'assignments': assignments}
			return render(request, 'display_names.html', context)
			#return HttpResponse(html)
		except ValueError:
			return HttpResponse("invalid")
	else:
		return render(request, 'form.html')

def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})

