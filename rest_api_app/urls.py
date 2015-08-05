from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api_app import views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^books/(?P<pk>[0-9]+)/$', views.book_detail),
    url(r'^$', views.post_list, name='post_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
