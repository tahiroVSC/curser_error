from rest_framework import serializers
from apps.Abonements.models import Abonement


class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        fields  = '__all__'
    
    freeze_ru = serializers.SerializerMethodField()
    freeze_ky = serializers.SerializerMethodField()
    
    def get_freeze_ru(self, obj):
        return f'{obj.mark_freeze}  {obj.freeze_ru}'
    def get_freeze_ky(self, obj):
        return f'{obj.mark_freeze}  {obj.freeze_ky}'
    
    trainer_ru = serializers.SerializerMethodField()
    trainer_ky = serializers.SerializerMethodField()
    
    def get_trainer_ru(self, obj):
        return f'{obj.mark_trainer}  {obj.trainer_ru}'
    def get_trainer_ky(self, obj):
        return f'{obj.mark_trainer}  {obj.trainer_ky}'
    
    guest_ru = serializers.SerializerMethodField()
    guest_ky = serializers.SerializerMethodField()
    
    def get_guest_ru(self, obj):
        return f'{obj.mark_trainer}  {obj.guest_ru}'
    def get_guest_ky(self, obj):
        return f'{obj.mark_trainer}  {obj.guest_ky}'


class AbonementValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    gruppa = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=None)
    photo = serializers.ImageField(use_url=True, required=False)
    weekdays = serializers.CharField(max_length=150)
    price_month = serializers.CharField(max_length=20)
    price_year = serializers.CharField(max_length=20)
