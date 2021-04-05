from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils import translation
from . import models



# Here is the Extra Context ditionary which is used in get_context_data of Views classes
def get_extra_context():
    extraContext = {
        'from_python': _('SOMETHING'),
        }
    return extraContext


# Index View
class IndexView(generic.TemplateView):
    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/BE-THEME/RTL/index.html"]
        # LTR languages
        else:
            return ["baseApp/BE-THEME/LTR/index.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        return context

######################### Art Gallery ################################
# Art Index View
class ArtGalleryIndexView(generic.TemplateView):
    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/POZO/RTL/art/index.html"]
        # LTR languages
        else:
            return ["baseApp/POZO/LTR/art/index.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # models
        context['featuredArts'] = models.Art.objects.filter(featured=True)
        return context

# About View
class ArtAboutMeView(generic.TemplateView):
    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/BE-THEME/RTL/about/art-about.html"]
        # LTR languages
        else:
            return ["baseApp/BE-THEME/LTR/about/art-about.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language Navbar
        return context

# Gallery View
class ArtPortfolioView(generic.TemplateView):
    def get_template_names(self):
        current_lang = translation.get_language()
        if current_lang == 'fa':
            return ["baseApp/POZO/RTL/art/art-portfolio.html"]
        else:
            return ["baseApp/POZO/LTR/art/art-portfolio.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())
        # It must be checked in the method not in attributes
        current_lang = translation.get_language()

        # Arts
        context['all_arts'] = models.Art.objects.filter(active__exact=True)
        return context

# Art Details
class ArtDetailView(generic.DetailView):
    context_object_name = 'the_art'
    model = models.Art

    def get_template_names(self):
        current_lang = translation.get_language()
        if current_lang == 'fa':
            return ["baseApp/POZO/RTL/art/art_detail.html"]
        else:
            return ["baseApp/POZO/LTR/art/art_detail.html"]

    def get_object(self, **kwargs):
        singleResult = self.model.objects.get(slug=self.kwargs['slug'], active=True)
        # To implement save method on the model which adds view count
        singleResult.save()
        return singleResult

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()

        context['slideContent'] = ""

        return context

######################### Interior Design ################################
# Design Index View
class InteriorDesignIndexView(generic.TemplateView):
    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/BE-THEME/RTL/design/index.html"]
        # LTR languages
        else:
            return ["baseApp/BE-THEME/LTR/design/index.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # models
        context['featuredDesigns'] = models.Design.objects.filter(featured=True)
        return context

# About View
class DesignAboutMeView(generic.TemplateView):
    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/BE-THEME/RTL/about/design-about.html"]
        # LTR languages
        else:
            return ["baseApp/BE-THEME/LTR/about/design-about.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language Navbar
        return context

# Portfolio View
class DesignPortfolioView(generic.TemplateView):
    def get_template_names(self):
        current_lang = translation.get_language()
        if current_lang == 'fa':
            return ["baseApp/POZO/RTL/design/design-portfolio.html"]
        else:
            return ["baseApp/POZO/LTR/design/design-portfolio.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())
        # It must be checked in the method not in attributes
        current_lang = translation.get_language()

        # Designs
        context['all_designs'] = models.Design.objects.filter(active__exact=True)
        return context

# Designs Details
class DesignDetailView(generic.DetailView):
    context_object_name = 'the_design'
    model = models.Design

    def get_template_names(self):
        current_lang = translation.get_language()
        if current_lang == 'fa':
            return ["baseApp/POZO/RTL/design/design_detail.html"]
        else:
            return ["baseApp/POZO/LTR/design/design_detail.html"]

    def get_object(self, **kwargs):
        singleResult = self.model.objects.get(slug=self.kwargs['slug'], active=True)
        # To implement save method on the model which adds view count
        singleResult.save()
        return singleResult

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()

        context['slideContent'] = ""

        return context
