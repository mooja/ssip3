# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.contrib.sitemaps.views import sitemap

from views import HomeView, contact_us
from views import HomeView

from .sitemaps import StaticViewSitmap, NewsSiteMap

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact_us$', contact_us, name='contact_us'),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^flatpages/', include('flatpages.urls', namespace='flatpages')),

    # robots.txt
    url(r'^robots\.txt$', 
        lambda r: HttpResponse('User-agent: *\nDisallow: /members/*', content_type='text/plain')),

    # sitemaps
    url(r'^sitemap\.xml$', sitemap, 
        {'sitemaps': {'static': StaticViewSitmap}},
        name='django.contrib.sitemaps.views.sitemap'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
