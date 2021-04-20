from django.contrib import admin
from django.db import models
from .models import (
                    Collection,
                    Art,
                    ArtImages,
                    Design,
                    DesignImages,
                    Banner
                    )


class CollectionAdmin(admin.ModelAdmin):

    list_filter = ['name']
    list_display = ['id', 'image_tag', 'name', 'active', 'display_order']
    list_editable = ['active', 'display_order']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['image_tag']

class ArtImagesInline(admin.TabularInline):
    model = ArtImages
    list_display = ['art', 'image_tag', 'image', 'active', 'display_order']
    list_editable = ['display_order']
    readonly_fields = ['image_tag']

class ArtAdmin(admin.ModelAdmin):

    list_filter = ['collection', 'title']
    list_display = ['id', 'image_tag', 'title', 'collection', 'active', 'featured']
    list_editable = ['active', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['image_tag']

    # other Inlines
    inlines = [
        ArtImagesInline,
    ]

class DesignImagesInline(admin.TabularInline):
    model = DesignImages
    list_display = ['design', 'image_tag', 'image', 'active', 'display_order']
    list_editable = ['display_order']
    readonly_fields = ['image_tag']

class DesignAdmin(admin.ModelAdmin):

    list_filter = ['title']
    list_display = ['id', 'image_tag', 'title', 'active', 'featured']
    list_editable = ['active', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['image_tag']

    # other Inlines
    inlines = [
        DesignImagesInline,
    ]

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'title', 'useFor', 'display_order', 'active']
    list_editable = ['useFor', 'active', 'display_order']
    readonly_fields = ['image_tag']



admin.site.register(Art, ArtAdmin)
admin.site.register(Design, DesignAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Banner, BannerAdmin)
