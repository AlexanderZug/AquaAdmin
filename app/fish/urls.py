from django.urls import path

from .views import FishListAPIView

urlpatterns = [
    path("", FishListAPIView.as_view(), name="fish-list"),
]
