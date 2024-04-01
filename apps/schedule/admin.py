from django.contrib import admin
from apps.schedule.models import Schedule
from modeltranslation.admin import TranslationAdmin


class ScheduleAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('work_time_ru', 'holiday_work_time_ru')}),
        (u'Ky', {'fields': ('work_time_ky', 'holiday_work_time_ky')})
    ]


admin.site.register(Schedule, ScheduleAdmin)

