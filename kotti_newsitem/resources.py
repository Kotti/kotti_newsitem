# -*- coding: utf-8 -*-

"""
Created on 2013-02-07
:author: Andreas Kaiser (disko)
:contributors: Jeff Pittman (geojeff)
"""

from datetime import date

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Document
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from zope.interface import implements

from kotti_newsitem import _


class NewsPage(Document):
    """ News page content type.

        A NewsPage is a full page display for news items, as compared to the
        recent news widget that be used in a slot. It works the same way as
        the recent news widget, using the same template.
    """

    implements(IDefaultWorkflow)

    id = Column(Integer(), ForeignKey('documents.id'), primary_key=True)

    type_info = Document.type_info.copy(
        name=u'NewsPage',
        title=u'News Page',
        add_view=u'add_newspage',
        addable_to=[u'Document', u'NewsPage'],
        selectable_default_views=[],
    )

    def __init__(self, **kwargs):

        super(NewsPage, self).__init__(**kwargs)


class NewsItem(Document):
    """ News item content type.

        A NewsItem is a plain document with only one additional attribute:
        ``publish_date``.
    """

    implements(IDefaultWorkflow)

    id = Column(
        Integer(),
        ForeignKey('documents.id'),
        primary_key=True
        )

    publish_date = Column(
        Date(),
        nullable=False,
        )

    type_info = Document.type_info.copy(
        name=u'NewsItem',
        title=_(u'News Item'),
        add_view=u'add_newsitem',
        addable_to=['Document', 'NewsPage', ],
        selectable_default_views=[],
        )

    def __init__(self, publish_date=None, **kwargs):

        super(NewsItem, self).__init__(**kwargs)

        self.publish_date = publish_date or date.today()
