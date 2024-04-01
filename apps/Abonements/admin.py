from django.contrib import admin
from apps.Abonements.models import Abonement
from modeltranslation.admin import TranslationAdmin


class AbonementAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'mark_freeze', 'freeze_ru', 'mark_trainer',
         'trainer_ru', 'mark_guest', 'guest_ru', 'time_ru', 'price_ru', 'special')}),
        (u'Ky', {'fields': ('title_ky', 'freeze_ky',
         'trainer_ky', 'guest_ky',  'time_ky', 'price_ky')})
    ]


admin.site.register(Abonement, AbonementAdmin)
