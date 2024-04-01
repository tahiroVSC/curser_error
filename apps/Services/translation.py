from modeltranslation.translator import translator, TranslationOptions
from apps.Services.models import Services

class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'note', 'hours_week')

translator.register(Services, ServicesTranslationOptions)
