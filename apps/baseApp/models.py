from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.html import mark_safe


# Variables
YES_NO_CHOICES = [(True, 'Yes'), (False, 'No')]
PAGE_CHOICES = [('HOME', 'Homepage'),
                ('ABOUT', 'About')]


class Banner(models.Model):
    image = models.ImageField(upload_to='baseApp/banners/', null=True, blank=True,
                                help_text='HOME: 990x750, ABOUT: any')
    title = models.CharField(max_length=110, null=True, blank=True)
    sub_title = models.CharField(max_length=110, null=True, blank=True)
    title_fa = models.CharField(max_length=110, null=True, blank=True)
    sub_title_fa = models.CharField(max_length=110, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    description_fa = models.TextField(max_length=200, null=True, blank=True)
    target_url = models.URLField(max_length = 700, null=True, blank=True)
    display_order = models.PositiveIntegerField(default=1, null=True, blank=True)
    useFor = models.CharField(max_length=50, choices=PAGE_CHOICES, null=True, blank=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=False)

    # Display Thumbnails
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))
    image_tag.short_description = 'Image'

    def __str__(self):
            return "{}: banner for {}".format(self.title, self.useFor)

    class Meta():
        ordering = ['display_order']

class Collection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_fa = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    description_fa = models.TextField(max_length=500, null=True, blank=True)
    image_main = models.ImageField(upload_to='baseApp/art/', null=True,
                                help_text='Less than 3MB')
    display_order = models.PositiveIntegerField(default=1, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, allow_unicode=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    created = models.DateField(editable=False)
    updated = models.DateField(editable=False, null=True)

    # Display Thumbnails
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image_main))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

    class Meta():
        ordering  = ['display_order']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        # Update Date
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Collection, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('baseApp:collections', args=(self.id,))

class Art(models.Model):
    collection = models.ForeignKey(Collection, related_name='collectionArts', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    title_fa = models.CharField(max_length=100, null=True, blank=True)
    description_1 = models.TextField(max_length=500, null=True, blank=True)
    description_2 = models.TextField(max_length=500, null=True, blank=True)
    description_fa_1 = models.TextField(max_length=500, null=True, blank=True)
    description_fa_2 = models.TextField(max_length=500, null=True, blank=True)
    description_fa_3 = models.TextField(max_length=500, null=True, blank=True)
    description_fa_4 = models.TextField(max_length=500, null=True, blank=True)
    image_main = models.ImageField(upload_to='baseApp/art/', null=True,
                                help_text='1080x1400 Less than 3MB')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, allow_unicode=True)
    original_availability = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    copy_print_avalability = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    featured = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    created = models.DateField(editable=False)
    updated = models.DateField(editable=False, null=True)
    view = models.PositiveIntegerField(editable=False, default=0)

    # Display Thumbnails
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image_main))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

    class Meta():
        ordering  = ['-created']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        # Update Date
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()

        # View count
        self.view += 1
        return super(Art, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('baseApp:project', args=(self.id,))

class ArtImages(models.Model):
    art = models.ForeignKey(Art, related_name='artImages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='baseApp/art/', null=True,
                                help_text='Image 1600x1100')
    display_order = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)

    # Display Thumbnails
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))
    image_tag.short_description = 'Image'

    class Meta():
        verbose_name_plural = "Art Images"
        ordering = ['display_order']


########### Design ###########
class Design(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    title_fa = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    description_fa = models.TextField(max_length=500, null=True, blank=True)
    image_main = models.ImageField(upload_to='baseApp/design/', null=True,
                                help_text='1240x800 Less than 3MB')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, allow_unicode=True)
    featured = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    created = models.DateField(editable=False)
    updated = models.DateField(editable=False, null=True)
    view = models.PositiveIntegerField(editable=False, default=0)

    # Display Thumbnails
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image_main))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

    class Meta():
        ordering  = ['-created']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        # Update Date
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()

        # View count
        self.view += 1
        return super(Design, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('baseApp:project', args=(self.id,))

class DesignImages(models.Model):
    art = models.ForeignKey(Design, related_name='designImages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='baseApp/design/', null=True,
                                help_text='Image 1600x1100')
    display_order = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)

    class Meta():
        verbose_name_plural = "Design Images"
        ordering = ['display_order']

    # Display Thumbnails
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))
    image_tag.short_description = 'Image'
