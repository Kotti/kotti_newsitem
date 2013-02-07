from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_newsitem')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_newsitem'

    settings['kotti.available_types'] += ' kotti_newsitem.resources.NewsItem'


def includeme(config):

    config.add_translation_dirs('kotti_newsitem:locale')
    config.scan(__name__)
