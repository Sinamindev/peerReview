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
## Documentation

## Design Choices
