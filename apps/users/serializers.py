from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "phone_number", "created_at", "age")

    def validate(self, values):
        if values['phone_number'] != +996:
            raise serializers.ValidationError({'phone_number : начните номер телефона с +996'})
        return values