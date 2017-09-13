#import os
#import requests
from django.shortcuts import render
from django.http import HttpResponse

from .peer_review import getPeerAssignments

# Create your views here.
def index(request):
	return render(request, 'form.html')
	#return HttpResponse('Hello from Python!')

def search(request):
	if request.method == 'POST': # check if requested method is POST
		assignments = [] # create empy list for assignments
		N = int(request.POST.get('peers', None)) # assign N with number of peers 
		M = int(request.POST.get('reviews', None)) # assign M with number of reviews
		try:
			# getPeerAssignments takes peers and reviews
			# getPeerAssignments returns list of peers assignments 
			assignments = getPeerAssignments(N,M)

			# pass context the assignments as dictionary
			context = {'assignments': assignments} 

			# render the HttpResponse request and display with assignments using display_names.html
			return render(request, 'display_names.html', context) 
		except ValueError:
			# return an "Invalid" HttpResponse if invalid input was received
			return HttpResponse("Invalid")
	else:
		# render form.html to allow user to input number of peers and reviewers
		return render(request, 'form.html')


