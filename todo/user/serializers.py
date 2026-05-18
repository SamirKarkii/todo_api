from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

    def validate_title(self, value):

        if len(value) < 5:

            raise serializers.ValidationError(
                "Title must be at least 5 characters"
            )

        return value
    
    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "description and title cannot be same "
            )
        return data