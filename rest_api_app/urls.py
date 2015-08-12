from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api_app import views

urlpatterns = [

    #splash landing page for api
    #url(r'^$', views.book_root),

    # redirects to looks listing and details
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^book/new/$', views.book_new, name='book_new'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
