
from django.conf import settings
from random import sample
from collections import deque

def html_table(lol):
	print( '<table>')
	for sublist in lol:
	  print( '  <tr><td>')
	  print( '    </td><td>')
	  print( '  </td></tr>')
	  print( '</table>')



def assignPeers(X, Y):
	RANGE = deque(range(X))
	foo = []
	for i in range(X):
		RANGE.popleft()
		foo.append(sample(RANGE, Y))
		RANGE.append(i)
	return foo
	# html = ("<H1>%d Peers <br/> %d Reviews</H1>"% (X, Y))
	# return HttpResponse(html)