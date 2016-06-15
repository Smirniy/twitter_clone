from django.test import TestCase
from django.contrib.auth import get_user_model
from twitter.models import Tweet

class TweetModelTestCase(TestCase):

	def setUp(self):
		user = get_user_model().objects.create_user('dummy')
		self.tweet = Tweet.objects.create(
			text='Some great tweet',
			user=user)

	def test_tweet_basic(self):
		self.assertEqual(self.tweet.user.username, 'dummy')
		self.assertEqual(self.tweet.text, 'Some great tweet')

