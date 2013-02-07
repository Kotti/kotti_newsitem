from kotti.resources import get_root

from kotti_newsitem.resources import NewsItem
from kotti_newsitem.views import NewsItemView


def test_views(db_session, dummy_request):

    root = get_root()
    content = NewsItem()
    root['content'] = content

    view = NewsItemView(root['content'], dummy_request)

    assert view.view() == {}
    assert view.alternative_view() == {}
