from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .base import urlpatterns as base_url_patterns

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("aquarium/", include("aquarium.urls")),
    path("fish/", include("fish.urls")),
]

urlpatterns += base_url_patterns
urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
