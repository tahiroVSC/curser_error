from django.contrib import admin
from apps.About.models import AboutUs
from modeltranslation.admin import TranslationAdmin

class AboutUsAdmin(TranslationAdmin):
     fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'desc_ru','image')}),
        (u'Ky', {'fields': ('title_ky', 'desc_ky')})
    ]

admin.site.register(AboutUs, AboutUsAdmin)