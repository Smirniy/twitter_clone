import random
from django import template

register = template.Library()

from account.models import User
from ..models import Tweet

@register.simple_tag
def total_tweets():
	return Tweet.objects.count()

@register.simple_tag
def total_users():
	return User.objects.count()

@register.inclusion_tag('tweets/random_tweet.html')
def show_random_tweet():
	tweets = Tweet.objects.all()
	length = len(tweets)
	if length:
		random_tweet = tweets[random.randint(0, length - 1)]
	else:
		random_tweet = None
	return {'random_tweet': random_tweet}
