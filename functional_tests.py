from django.test import LiveServerTestCase
from selenium import webdriver

class TwitterTestCase(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(2)

	def test_can_view_tweets(self):
		pass
