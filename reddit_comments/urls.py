from django.conf.urls import patterns, url

urlpatterns = patterns('reddit_comments.views',
    url(r'', 'index')
)