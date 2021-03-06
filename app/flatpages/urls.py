# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import PageDetailView, AboutView, ServiceProvidersView, MinutesView

urlpatterns = patterns('',
    url(
        regex=r'^about/$',
        view=AboutView.as_view(),
        name='about'
    ),
    url(
        regex=r'^service-providers/$',
        view=ServiceProvidersView.as_view(),
        name='service-providers'
    ),
    url(
        regex=r'^minutes/$',
        view=MinutesView.as_view(),
        name='minutes'
    ),
    url(
        regex=r'^(?P<slug>[\w_-]+)/$',
        view=PageDetailView.as_view(),
        name='page-detail'
    ),
)
