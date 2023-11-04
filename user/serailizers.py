from rest_framework import serializers

from .models import UserModel


class UserSeralizer(serializers.ModelSerializer):
    ads_count = serializers.IntegerField()

    class Meta:
        model = UserModel
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'balance',
            'bonus',
            'ads_count'
        ]


class UserBalanceSerailizer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = UserModel
        fields = [
            'id',
            'username',
            'balance',
        ]
