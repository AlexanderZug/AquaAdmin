from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Aquarium
from .serializers import AquariumListSerializer


class AquariumListView(ListAPIView):
    queryset = Aquarium.objects.all()
    serializer_class = AquariumListSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="List [Aquarium]",
        description="List of all aquariums",
        responses={
            200: AquariumListSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
