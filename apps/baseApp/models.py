from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils import timezone

# Variables
YES_NO_CHOICES = [(True, 'Yes'), (False, 'No')]


class Art(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    title_fa = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description_1 = models.TextField(max_length=500, unique=True, null=True, blank=True)
    description_2 = models.TextField(max_length=500, unique=True, null=True, blank=True)
    description_fa_1 = models.TextField(max_length=500, unique=True, null=True, blank=True)
    description_fa_2 = models.TextField(max_length=500, unique=True, null=True, blank=True)
    image_main = models.ImageField(upload_to='baseApp/art/', null=True,
                                help_text='Less than 3MB')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, allow_unicode=True)
    original_availability = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    copy_print_avalability = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    featured = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    created = models.DateField(editable=False)
    updated = models.DateField(editable=False, null=True)
    view = models.PositiveIntegerField(editable=False, default=0)

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

    class Meta():
        verbose_name_plural = "Art Images"
        ordering = ['display_order']


########### Design ###########
class Design(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    title_fa = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(max_length=500, unique=True, null=True, blank=True)
    description_fa = models.TextField(max_length=500, unique=True, null=True, blank=True)
    image_main = models.ImageField(upload_to='baseApp/design/', null=True,
                                help_text='Less than 3MB')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, allow_unicode=True)
    featured = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    created = models.DateField(editable=False)
    updated = models.DateField(editable=False, null=True)
    view = models.PositiveIntegerField(editable=False, default=0)

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
