from django.db import models
from django.conf import settings

class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tweets')
	text = models.CharField(max_length=140, blank=False)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} on {}'.format(self.user, self.created)
