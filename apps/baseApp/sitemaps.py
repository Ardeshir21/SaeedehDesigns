from django.utils import timezone
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.baseApp.models import Art, Collection, Design
from django.db.models import F

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    protocol = 'https'
    i18n = True

    def items(self):
        return ['baseApp:index', 'baseApp:about_me', 'baseApp:art_index',
         'baseApp:collections', 'baseApp:design_index', 'baseApp:design_portfolio' ]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # This part check between created and updated date of lastest Project and use the latest date
        latest_updated_item = Art.objects.all().order_by(F('updated').desc(nulls_last=True))[0]
        latest_created_item = Art.objects.all().order_by(F('created').desc(nulls_last=True))[0]
        if latest_updated_item.updated:
            if latest_updated_item.updated >= latest_created_item.created:
                latest_item = latest_updated_item
                return latest_item.updated
            else:
                # Use the last created of Asset for each page
                latest_item = latest_created_item
                return latest_item.created
        else:
            latest_item = latest_created_item
            return latest_item.created

# Art sitemap
class ArtSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Art.objects.all()

    def lastmod(self, item):
        if item.updated:
            return item.updated
        else: return item.created

# Collection Page
class CollectionSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Collection.objects.all()

    def lastmod(self, item):
        # This part check between created and updated date of lastest Asset and use the latest date
        latest_updated_item = Art.objects.all().order_by(F('updated').desc(nulls_last=True))[0]
        latest_created_item = Art.objects.all().order_by(F('created').desc(nulls_last=True))[0]
        if latest_updated_item.updated:
            if latest_updated_item.updated >= latest_created_item.created:
                latest_item = latest_updated_item
                return latest_item.updated
            else:
                # Use the last created of Asset for each page
                latest_item = latest_created_item
                return latest_item.created
        else:
            latest_item = latest_created_item
            return latest_item.created

# Design sitemap
class DesignSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Design.objects.all()

    def lastmod(self, item):
        if item.updated:
            return item.updated
        else: return item.created
