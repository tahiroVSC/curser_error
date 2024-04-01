from modeltranslation.translator import translator, TranslationOptions
from apps.schedule.models import Schedule


class ScheduleTranslationOptions(TranslationOptions):
    fields = ('work_time', 'holiday_work_time')


translator.register(Schedule, ScheduleTranslationOptions)
