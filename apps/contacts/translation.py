from modeltranslation.translator import translator, TranslationOptions
from apps.contacts.models import Contact


class ContactTranslationOptions(TranslationOptions):
    fields = ('address', )


translator.register(Contact, ContactTranslationOptions)
