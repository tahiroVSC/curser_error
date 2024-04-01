from django.contrib import admin
from django.db import models
from apps.Offering.models import Offering, Icons

from modeltranslation.admin import TranslationAdmin

class OfferingAdmins(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'image', 'hide',)}),
        (u'Ky', {'fields': ('title_ky',)})
    ]



admin.site.register(Offering, OfferingAdmins)
admin.site.register(Icons)