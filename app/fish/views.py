from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from .models import Fish
from .serializers import FishListSerializer, FishCreateSerializer


class FishListAPIView(ListAPIView):
    queryset = Fish.objects.all().prefetch_related("sales", "died")
    serializer_class = FishListSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="List [Fish]",
        description="List of all fish",
        responses={
            200: FishListSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FishCreateAPIView(CreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishCreateSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Create [Fish]",
        description="Create a fish",
        responses={
            201: FishCreateSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
