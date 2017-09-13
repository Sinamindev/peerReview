#import os
#import requests
from django.shortcuts import render
from django.http import HttpResponse

from .peer_review import assignPeers

# Create your views here.
def index(request):
	return render(request, 'form.html')
	#return HttpResponse('Hello from Python!')

def search(request):
	if request.method == 'POST':
		assignments = []
		X = int(request.POST.get('peers', None))
		Y = int(request.POST.get('reviews', None))
		try:
			assignments = assignPeers(X,Y)
			context = {'assignments': assignments}
			return render(request, 'display_names.html', context)
		except ValueError:
			return HttpResponse("invalid")
	else:
		return render(request, 'form.html')


