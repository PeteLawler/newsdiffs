from django.conf.urls import url
from frontend.views import (about, article_history, article_history_feed,
                            browse, contact, diffview, examples, feed,
                            front, json_view, old_diffview, press, subscribe,
                            upvote)

urlpatterns = [
  # These are deprecated, and meant to preserve legacy URLs:
  url(r'^diffview/$', old_diffview),
  url(r'^article-history/$', article_history, name='article_history'),

  # These are current:
  url(r'^upvote/$', upvote, name='upvote'),
  url(r'^diff/(?P<vid1>\d+)/(?P<vid2>\d+)/(?P<urlarg>.*)$',
      diffview, name='diffview'),
  url(r'^about/$', about, name='about'),
  url(r'^browse/$', browse, name='browse'),
  url(r'^browse/(.*)$', browse, name='browse'),
  url(r'^feed/browse/(.*)$', feed, name='feed'),
  url(r'^contact/$', contact, name='contact'),
  url(r'^examples/$', examples, name='examples'),
  url(r'^subscribe/$', subscribe, name='subscribe'),
  url(r'^press/$', press, name='press'),
  url(r'^feed/article-history/(.*)$', article_history_feed,
      name='article_history_feed'),
  url(r'^article-history/(?P<urlarg>.*)$', article_history,
      name='article_history'),
  url(r'^json/view/(?P<vid>\d+)/?$', json_view),
  url(r'^$', front, name='root'),
]
