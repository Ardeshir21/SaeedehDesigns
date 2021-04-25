from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views, sitemaps

app_name = 'baseApp'

sitemaps_dict = {'Static_sitemap': sitemaps.StaticSitemap,
                'Art_sitemap': sitemaps.ArtSitemap,
                'Collection_sitemap': sitemaps.CollectionSitemap,
                'Design_sitemap': sitemaps.DesignSitemap,
                }

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about-me/', views.ArtAboutMeView.as_view(), name='about_me'),
    # Art
    path('art-gallery/', views.ArtGalleryIndexView.as_view(), name='art_index'),
    # path('art-gallery/about-me/', views.ArtAboutMeView.as_view(), name='art_about_me'),
    path('art-gallery/collections/', views.CollectionsView.as_view(), name='collections'),
    path('art-gallery/collections/<slug:collection_slug>/', views.ArtPortfolioView.as_view(), name='art_portfolio'),
    path('art-gallery/collections/<slug:collection_slug>/<slug:art_slug>', views.ArtDetailView.as_view(), name='art_detail'),
    # Interior Design
    path('interior-design/', views.InteriorDesignIndexView.as_view(), name='design_index'),
    # path('interior-design/about-me/', views.DesignAboutMeView.as_view(), name='design_about_me'),
    path('interior-design/portfolio/', views.DesignPortfolioView.as_view(), name='design_portfolio'),
    path('interior-design/portfolio/<slug:slug>', views.DesignDetailView.as_view(), name='design_detail'),

    # This is for sitemap.xml
    path('saeedeh-sitemap.xml', sitemap, {'sitemaps': sitemaps_dict},
     name='django.contrib.sitemaps.views.sitemap'),
]


# handler404 = 'apps.baseApp.views.error_404'
# handler500 = 'apps.baseApp.views.error_500'
