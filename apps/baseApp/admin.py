from django.contrib import admin
from django.db import models
from .models import (
                    Art,
                    ArtImages,
                    Design,
                    DesignImages
                    )



class ArtImagesInline(admin.TabularInline):
    model = ArtImages
    list_display = ['art', 'image', 'active', 'display_order']
    list_editable = ['display_order']

class ArtAdmin(admin.ModelAdmin):

    list_filter = ['title']
    list_display = ['id', 'title', 'active', 'featured']
    list_editable = ['active', 'featured']
    prepopulated_fields = {'slug': ('title',)}

    # other Inlines
    inlines = [
        ArtImagesInline,
    ]

class DesignImagesInline(admin.TabularInline):
    model = DesignImages
    list_display = ['design', 'image', 'active', 'display_order']
    list_editable = ['display_order']

class DesignAdmin(admin.ModelAdmin):

    list_filter = ['title']
    list_display = ['id', 'title', 'active', 'featured']
    list_editable = ['active', 'featured']
    prepopulated_fields = {'slug': ('title',)}

    # other Inlines
    inlines = [
        DesignImagesInline,
    ]
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'useFor', 'active']
#     list_editable = ['useFor', 'active']



admin.site.register(Art, ArtAdmin)
admin.site.register(Design, DesignAdmin)
# admin.site.register(Banner, BannerAdmin)
