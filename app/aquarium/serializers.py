from rest_framework import serializers

from .models import Aquarium


class AquariumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aquarium
        fields = "__all__"
