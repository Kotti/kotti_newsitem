# -*- coding: utf-8 -*-

from colander import SchemaNode
from colander import String
from kotti.views.edit.content import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_newsitem import _
from kotti_newsitem.resources import NewsItem
from kotti_newsitem.fanstatic import kotti_newsitem


class NewsItemSchema(ContentSchema):
    """Schema for add / edit forms of NewsItem"""

    example_attribute = SchemaNode(
        String(),
        title=_(u'Example Attribute'),
        missing=u"",
    )


@view_config(name=NewsItem.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class NewsItemAddForm(AddFormView):

    schema_factory = NewsItemSchema
    add = NewsItem
    item_type = _(u"NewsItem")


@view_config(name='edit',
             context=NewsItem,
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class NewsItemEditForm(EditFormView):

    schema_factory = NewsItemSchema


@view_defaults(context=NewsItem, permission='view')
class NewsItemView(object):
    """View(s) for NewsItem"""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name='view',
                 renderer='kotti_newsitem:templates/NewsItem.pt')
    def view(self):

        kotti_newsitem.need()

        return {}

    @view_config(name='alternative-view',
                 renderer='kotti_newsitem:templates/NewsItem-alternative.pt')
    def alternative_view(self):

        return {}
