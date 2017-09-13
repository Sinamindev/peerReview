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
The peer assignment algorithm runs at O(NM) time complexity, which is Quadratic.

This is because the for-loop runs N times and contains a call to random.sample(), which has an O(M) time complexity.

Documentation for [random.sample()](https://hg.python.org/cpython/file/ab500b297900/Lib/random.py#l267)

## Design Choices
We use a list to store review assignments for each peer

We Use a deque to randomly sample M number of reviews to assign to each peer
 
A deque is used so we can pop out the value corresponding to the peer being assigned before randomly choosing from the remaining values in the deque in order to prevent two things:
 1. Prevents assigning a peer to themselves
 2. Prevents assigning duplicate reviews to the same peer

At the end of every loop, the peer value that was popped out of the deque is appended to the back

The list of assigned reviews is returned after every peer has been randomly assigned reviews
