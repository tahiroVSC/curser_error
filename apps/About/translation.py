from modeltranslation.translator import translator, TranslationOptions
from apps.About.models import AboutUs

class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')

translator.register(AboutUs, AboutUsTranslationOptions)