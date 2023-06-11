from .models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    time_passed = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ["id", "title", "description", "created_at", "user", "time_passed"]

    def get_time_passed(self, obj):
        return obj.time_passed()
