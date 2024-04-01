from django.contrib import admin

from apps.Review.models import Review
from modeltranslation.admin import TranslationAdmin

class ReviewAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('photo', 'name_ru', 'jobtitle_ru', 'description_ru' )}),
        (u'Ky', {'fields': ('name_ky', 'jobtitle_ky', 'description_ky')})
    ]

admin.site.register(Review, ReviewAdmin)