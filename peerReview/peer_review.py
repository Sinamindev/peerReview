from django.conf import settings
from random import sample
from collections import deque

# getPeerAssignments function
# IN: N == number of peers
# IN: M == number of reviews
# OUT: assignments == list of assigned reviews for each peer
# logic:	We use a list to store review assignments for each peer
# 			We Use a deque to randomly sample M number of reviews to assign to each peer
#			A deque is used so we can pop out the value corresponding to the peer being assigned,
#	 		 before randomly choosing from the remaining values in the deque in order to prevent two things
#			 1. Prevents assigning a peer to themselves
#			 2. Prevents assigning duplicate reviews to the same peer
#			At the end of every loop, the peer value that was popped out of the deque is appended to the back
#			The list of assigned reviews is returned after every peer has been randomly assigned reviews
def getPeerAssignments(N, M):
	RANGE = deque(range(N+1)) # create deque of size N+1
	RANGE.popleft() # pop the 0 value out of the deque
	assignments = [] # create empy list for assignments

	# execute loop for each peer starting from 1 and including the last peer
	for i in range(1, N+1):
		RANGE.popleft() # pop the first value out of the deque
		assignments.append(sample(RANGE, M)) # append a list of M random values from RANGE deque
		RANGE.append(i) # append the previously popped off value to the back of the RANGE deque
	return assignments # return assignments list containing list of assigned reviews for each peer

# SAMPLE OUTPUT: N == 5, M == 3
# ------------------------------------------------------------------------------------------------
# deque([0, 1, 2, 3, 4, 5])									# RANGE = deque(range(N+1))
# deque([1, 2, 3, 4, 5])									# RANGE.popleft()
# FOR-LOOP
# deque([2, 3, 4, 5])										# RANGE.popleft()
# [[3, 5, 2]]												# assignments.append(sample(RANGE, M))
# deque([2, 3, 4, 5, 1])									# RANGE.appen d(i)
# deque([3, 4, 5, 1])										# RANGE.popleft()
# [[3, 5, 2], [3, 5, 4]]									# assignments.append(sample(RANGE, M))
# deque([3, 4, 5, 1, 2])									# RANGE.append(i)
# deque([4, 5, 1, 2])										# RANGE.popleft()
# [[3, 5, 2], [3, 5, 4], [5, 1, 2]]							# assignments.append(sample(RANGE, M))
# deque([4, 5, 1, 2, 3])									# RANGE.append(i)
# deque([5, 1, 2, 3])										# RANGE.popleft()
# [[3, 5, 2], [3, 5, 4], [5, 1, 2], [2, 5, 3]]				# assignments.append(sample(RANGE, M))
# deque([5, 1, 2, 3, 4])									# RANGE.append(i)
# deque([1, 2, 3, 4])										# RANGE.popleft()
# [[3, 5, 2], [3, 5, 4], [5, 1, 2], [2, 5, 3], [3, 1, 4]]	# assignments.append(sample(RANGE, M))
# deque([1, 2, 3, 4, 5])									# RANGE.append(i)
# deque([1, 2, 3, 4, 5])									# RANGE.popleft()
# [[3, 5, 2], [3, 5, 4], [5, 1, 2], [2, 5, 3], [3, 1, 4]]	# assignments.append(sample(RANGE, M))

