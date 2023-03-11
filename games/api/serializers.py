from rest_framework import serializers
from games.models import Developer, Game
from datetime import date


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id']

    def validate_publication_date(self, date_value):
        today = date.today()
        if date_value > today:
            raise serializers.ValidationError('Yayımlanma tarihi ileri bir tarih olamaz!')
        return date_value


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'

    def validate_age(self, data_value):
        if data_value < 21:
            raise serializers.ValidationError(f'Developer yaşı 21 den küçük olamaz')
        return data_value
