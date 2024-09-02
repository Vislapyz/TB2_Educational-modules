from rest_framework import serializers

from modules.models import Module


class ModuleSerializer(serializers.ModelSerializer):
    "Сериализатор для модели Modules"

    class Meta:
        model = Module
        fields = '__all__'