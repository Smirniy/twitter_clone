from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', 
   	views.all_tweets, 
   	name='index'),
   url(r'^feed',
   	views.user_feed,
   	name='user_feed'),
   url(r'^users/(?P<username>\w+)/$',
   	views.user_page,
   	name='user_page'),
   url(r'^follow/$', 
   	views.follow, 
   	name='follow'),
   url(r'^new_tweet$', 
   	views.new_tweet, 
   	name='new_tweet'),
]
