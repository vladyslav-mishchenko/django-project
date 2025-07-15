from rest_framework.permissions import IsAdminUser
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


class AdminOnlySpectacularAPIView(SpectacularAPIView):
    permission_classes = [IsAdminUser]


class AdminOnlySwaggerView(SpectacularSwaggerView):
    permission_classes = [IsAdminUser]


class AdminOnlyRedocView(SpectacularRedocView):
    permission_classes = [IsAdminUser]
