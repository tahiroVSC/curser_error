from django.contrib import admin
from apps.contacts.models import Contact
from modeltranslation.admin import TranslationAdmin


class ContactAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('first_number', 'second_number', 'email', 'address_ru', 'links')}),
        (u'Ky', {'fields': ('address_ky', )})
    ]


admin.site.register(Contact, ContactAdmin)
