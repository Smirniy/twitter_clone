from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Follow(models.Model):
	user_from = models.ForeignKey(User, related_name="who_follows")
	user_to = models.ForeignKey(User, related_name="who_is_followed")

	def __str__(self):
		return '{} follows {}'.format(self.following, self.follower)

User.add_to_class('following',
				models.ManyToManyField('self',
									through=Follow,
									related_name='followers',
									symmetrical=False))