from django.conf import settings
from random import sample
from collections import deque

def assignPeers(X, Y):
	RANGE = deque(range(X))
	foo = []
	for i in range(X):
		RANGE.popleft()
		foo.append(sample(RANGE, Y))
		RANGE.append(i)
	return foo
