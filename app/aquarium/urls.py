from django.urls import path

from .views import AquariumListAPIView

urlpatterns = [
    path("", AquariumListAPIView.as_view(), name="aquarium-list"),
]
