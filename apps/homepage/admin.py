from django.contrib import admin
from apps.homepage.models import HomePage
from modeltranslation.admin import TranslationAdmin


# class HomePageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'subtitle', 'photo')


class HomePageTranslationAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'subtitle_ru','photo')}),
        (u'Ky', {'fields': ('title_ky','subtitle_ky')})
    ]


# Register your models here.
admin.site.register(HomePage, HomePageTranslationAdmin)
