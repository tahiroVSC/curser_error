from modeltranslation.translator import translator, TranslationOptions
from apps.Abonements.models import Abonement

class AbonementTranslationOptions(TranslationOptions):
    fields = ('title', 'freeze', 'trainer', 'guest', 'time', 'price')

translator.register(Abonement, AbonementTranslationOptions)