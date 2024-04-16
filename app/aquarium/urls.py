from django.urls import path

from .views import AquariumListView

urlpatterns = [
    path("", AquariumListView.as_view(), name="aquarium-list"),
]
