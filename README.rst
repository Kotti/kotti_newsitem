==============
kotti_newsitem
==============

|build status production|

News Item and News Page content types for Kotti.

This package provides:

-   a ``NewsItem`` content type that is just a Document with a different
    default view,

-   a ``NewsPage`` content type that is a Document used for listing news items
    on a "full" page-style display,

-   a ``RecentNews`` widget (that can be assigned to a slot) showing (by
    default) the 5 most recent, published ``NewsItems`` and

-   an ``all_news`` view that shows all ``News Items`` in your site,
    chronologically ordered.

`Find out more about Kotti`_

Setup
=====

To activate the ``kotti_newsitem`` add-on in your Kotti site, you need to add
an entry to the ``kotti.configurators`` setting in your Paste Deploy config.
If you don't have a ``kotti.configurators`` option, add one.  The line in your
``[app:main]`` (or ``[app:kotti]``, depending on how you setup Fanstatic)
section could then look like this::

    kotti.configurators = kotti_newsitem.kotti_configure

Configuration
=============

A good approach for managing news items on your site is to make a private
container document for holding the actual news items. It is a good idea to
organize them somehow, as by year::

    news-items
        2013
            news-item-foo
            news-item-bar
            ...
        2014
            ...

This is primarily to help organize for the content creator; this would mainly
be for storing the news items, not necessarily for presenting them. Display of
news items as a list can be done either by adding a NewsPage or by using the
recent news widget. Of course, you may choose to publish the actual storage
hierarchy of the news items if you prefer.

.. Note:: News items need to be set to ``Public`` state to show up in either
          the recent news widget or on a NewsPage.

News Page
---------

Add a NewsPage, usually at the top-level of your site, if you want a full-page
style list display of recent news items. Control the number of recent items
shown with::

    kotti_newsitem.num_news = 10

At the bottom of the list of news items, regardless of the number of most
recent news items listed, is a link to a page for ``All News``, where all news
items are shown.

Recent News Widget
------------------

If you want the ``RecentNews`` widget to show up in your site, either in place
of a dedicated NewsPage or to augment it, you have to add a line like this to
enable the recent news widget::

    kotti_newsitem.widget.slot = right

The for a list of available slots in a default Kotti site see the
`kotti.view.slots API docs`_

To change the default number of news items shown in the widget (5), add a line
like this::

    kotti_newsitem.widget.num_news = 10

.. Note:: kotti_newsitem.num_news controls the number of items shown on a
          NewsPage; kotti_newsitem.widget.num_news does the same for the
          widget. You might have the page set to show 10, but the widget
          only 2, for example.

Development
===========

|build status master|

Contributions to ``kotti_newsitem`` are highly welcome. Just clone its Github
repository and submit your contributions as pull requests.


.. |build status production| image:: https://travis-ci.org/Kotti/kotti_newsitem.png?branch=production
.. |build status master| image:: https://travis-ci.org/Kotti/kotti_newsitem.png?branch=master
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _kotti.view.slots API docs: http://kotti.readthedocs.org/en/latest/_modules/kotti/views/slots.html#assign_slot
