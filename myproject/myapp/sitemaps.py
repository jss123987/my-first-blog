from django.contrib.sitemaps import Sitemap
from myapp.models import Post
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)

class HelloSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

