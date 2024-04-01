from django.contrib import admin

from apps.Services.models import Services
from modeltranslation.admin import TranslationAdmin

class ServicesAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'note_ru', 'hours_week_ru', 'price' )}),
        (u'Ky', {'fields': ('title_ky', 'note_ky', 'hours_week_ky',)})
    ]

admin.site.register(Services, ServicesAdmin)