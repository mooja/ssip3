from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from news.models import NewsEntry


class StaticViewSitmap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['home', 'flatpages:about', 'flatpages:service-providers', 'members:member_list']

    def location(self, item):
        return reverse(item)


class NewsSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return NewsEntry.objects.all().order_by('-pub_date')

    def lastmod(self, obj):
        return obj.pub_date
