# Heroku Django App: Peer Review
 

## How to Use

 1. Enter total number of peers
 2. Enter total number of reviewers
 3. Click Submit

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:Sinamindev/peerReview.git
$ cd peerReview

$ pipenv install

$ createdb peerReview

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
## Documentation for assinging Peers to Review videos

The algorithm can be found in peer_review.py

The peer assignment algorithm runs at O(NM) time complexity, which is Quadratic.

This is because the for-loop runs N times and contains a call to random.sample(), which has an O(M) time complexity.

Documentation for [random.sample()](https://hg.python.org/cpython/file/ab500b297900/Lib/random.py#l267)

I believe this is the optimal method of random assignment. 

The trade-off for an algorithm like this, is that it's possible for some Peers to have their videos be reviewed more than others. For example, if we have 5 Peers and need each Peer to review 1 video, then it's technically possible that every Peer but one will review the same video, while the rest of the videos never get a review. This situation interests me and I plan on finding a solution to better spread out the reviews more fairly, while not sacrificing too much time complexity.  

## Design Choices
A list is used to store separate lists for each Peer(N) and their corresponding assigned Reviews(M)  

A deque is created with values rangeing from 1 to N, and used to randomly sample M number of reviews to assign to each Peer
 
A deque is used so we can pop out the value corresponding to the Peer currently being assigned Reviews before randomly choosing from the remaining values in the deque, which prevents two things:
 1. Prevents assigning a Peer to Review themselves
 2. Prevents assigning duplicate Reviews to the same Peer

At the end of every loop, the Peer value that was popped out of the deque is appended to the back

The list of assigned Reviews is returned after every Peer has been randomly assigned Reviews

## Sample Output for Algorithm

SAMPLE OUTPUT: N == 5, M == 3

    deque([0, 1, 2, 3, 4, 5])                               # RANGE = deque(range(N+1))
    deque([1, 2, 3, 4, 5])                                  # RANGE.popleft()
FOR-LOOP
    
    deque([2, 3, 4, 5])                                     # RANGE.popleft()
    [[3, 5, 2]]                                             # assignments.append(sample(RANGE, M))
    deque([2, 3, 4, 5, 1])                                  # RANGE.appen d(i)
    deque([3, 4, 5, 1])                                     # RANGE.popleft()
    [[3, 5, 2], [3, 5, 4]]                                  # assignments.append(sample(RANGE, M))
    deque([3, 4, 5, 1, 2])                                  # RANGE.append(i)
    deque([4, 5, 1, 2])                                     # RANGE.popleft()
    [[3, 5, 2], [3, 5, 4], [5, 1, 2]]                       # assignments.append(sample(RANGE, M))
    deque([4, 5, 1, 2, 3])                                  # RANGE.append(i)
    deque([5, 1, 2, 3])                                     # RANGE.popleft()
    [[3, 5, 2], [3, 5, 4], [5, 1, 2], [2, 5, 3]]            # assignments.append(sample(RANGE, M))
    deque([5, 1, 2, 3, 4])                                  # RANGE.append(i)
    deque([1, 2, 3, 4])                                     # RANGE.popleft()
    [[3, 5, 2], [3, 5, 4], [5, 1, 2], [2, 5, 3], [3, 1, 4]] # assignments.append(sample(RANGE, M))
    deque([1, 2, 3, 4, 5])                                  # RANGE.append(i)
    deque([1, 2, 3, 4, 5])                                  # RANGE.popleft()
    [[3, 5, 2], [3, 5, 4], [5, 1, 2], [2, 5, 3], [3, 1, 4]] # assignments.append(sample(RANGE, M))
