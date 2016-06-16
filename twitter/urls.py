from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', 
   	views.AllTweetsListView.as_view(), 
   	name='index'),
   url(r'^feed',
   	views.UserFeedListView.as_view(),
   	name='user_feed'),
   url(r'^users/(?P<username>\w+)/$',
   	views.UserPageListView.as_view(),
   	name='user_page'),
   url(r'^new_tweet$', 
      views.NewTweetView.as_view(), 
      name='new_tweet'),
   url(r'^follow/$', 
   	views.follow, 
   	name='follow'),
]
