from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user_name', 'activity_type', 'duration_minutes', 'created_at']

    def get_id(self, obj):
        return str(obj.pk)
