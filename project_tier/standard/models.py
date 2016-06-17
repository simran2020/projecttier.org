from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch.index import SearchField

from project_tier.blocks import BodyBlock


class StandardIndexPage(Page):
    introductory_headline = models.TextField()

    @property
    def children(self):
        return self.get_children().specific().live()

    search_fields = Page.search_fields + [
        SearchField('introductory_headline')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introductory_headline', classname='full')
    ]


class StandardPage(Page):
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.')
    overview = RichTextField(help_text='Give a general overview of what this topic is about. Limit yourself to 3 paragraphs.')
    body = StreamField(BodyBlock())
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.')

    @property
    def parent(self):
        return self.get_parent().specific

    search_fields = Page.search_fields + [
        SearchField('introductory_headline'),
        SearchField('overview'),
        SearchField('listing_abstract'),
        SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('listing_abstract', classname='full'),
        FieldPanel('introductory_headline', classname='full'),
        FieldPanel('overview', classname='full'),
        StreamFieldPanel('body'),
    ]

    subpage_types = []