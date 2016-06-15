from django.test import TestCase, RequestFactory
from django.core.paginator import Page
from django.contrib.auth import get_user_model
from twitter.models import Tweet
from twitter.views import all_tweets, user_feed

class AllTweetsViewTestCase(TestCase):

	def setUp(self):
		self.factory = RequestFactory()
		user = get_user_model().objects.create_user('dummy')
		self.first_tweet = Tweet.objects.create(
			user=user,
			text='Some dummy text')
		self.second_tweet = Tweet.objects.create(
			user=user,
			text='Greatest tweet ever')

	def test_all_tweets_view_basic(self):
		request = self.factory.get('/')
		with self.assertTemplateUsed('tweets/list.html'):
			response = all_tweets(request)
			self.assertEqual(response.status_code, 200)

	def test_all_tweets_view_returns_pages(self):
		response = self.client.get('/')
		self.assertIs(
			type(response.context['items']),
			Page
		)

class UserFeedViewTestCase(TestCase):

	def setUp(self):
		self.factory = RequestFactory()

	def test_user_feed_view_requires_login(self):
		pass
