from django.urls import path

from .views import FishListAPIView, FishCreateAPIView

urlpatterns = [
    path("", FishListAPIView.as_view(), name="fish-list"),
    path("new/fish/", FishCreateAPIView.as_view(), name="fish-create"),
]
