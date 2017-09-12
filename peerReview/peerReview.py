from random import sample
from collections import deque

X = 5 #range(5)[::1] # [0, 1, 2, 3, 4]

Y = 3

RANGE = deque(range(X))
foo = []

for i in range(X):
    RANGE.popleft()
    foo.append(sample(RANGE, Y))
    RANGE.append(i)

print(RANGE)
print(foo)