from modeltranslation.translator import translator, TranslationOptions

from apps.homepage.models import HomePage


class HomePageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',)


translator.register(HomePage, HomePageTranslationOptions)
