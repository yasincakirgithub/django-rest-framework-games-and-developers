from rest_framework import serializers
from games.models import Developer, Game
from datetime import datetime
from datetime import date
from django.utils.timesince import timesince


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'
        # fields = ['']
        # exclude = ['']
        read_only_fields = ['id']

    def validate_publication_date(self, date_value):
        today = date.today()
        if date_value > today:
            raise serializers.ValidationError('Yayımlanma tarihi ileri bir tarih olamaz!')
        return date_value

class DeveloperSerializer(serializers.ModelSerializer):

    games = GameSerializer(many=True, read_only=True)
    #games = serializers.HyperlinkedRelatedField(
    #    many=True,
    #    read_only=True,
    #    view_name='game-detail',
    #)

    class Meta:
        model = Developer
        fields = '__all__'