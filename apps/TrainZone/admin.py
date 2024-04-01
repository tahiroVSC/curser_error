from django.contrib import admin
from django.db import models
from .models import TrainZone, TrainZoneImage
from modeltranslation.admin import TranslationAdmin

# Model for storing additional train zone images

# Inline admin for TrainZoneExtraImage
class TrainZoneExtraImageAdmin(admin.StackedInline):
    model = TrainZoneImage
    extra = 0

# Admin configuration for TrainZone (using modeltranslation)
class TrainZoneAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'description_ru', )}),
        (u'Ky', {'fields': ('title_ky', 'description_ky',)}),
    ]
    inlines = [TrainZoneExtraImageAdmin]

# Ensure only one registration for TrainZone
@admin.register(TrainZone)  # Use the @admin.register decorator for clarity
class TrainZoneAdmin(TrainZoneAdmin):  # Reuse the existing class
    pass  # No additional configuration needed
