from rest_framework import serializers

from .models import Fish, Sale, Died


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = [
            "id",
            "amount",
            "price",
            "created_at",
        ]


class DiedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Died
        fields = [
            "id",
            "amount",
            "created_at",
        ]


class FishListSerializer(serializers.ModelSerializer):
    sales = SaleSerializer(many=True)
    died = DiedSerializer(many=True)

    class Meta:
        model = Fish
        fields = [
            "id",
            "name",
            "amount",
            "image",
            "created_at",
            "is_available",
            "sales",
            "died",
        ]
