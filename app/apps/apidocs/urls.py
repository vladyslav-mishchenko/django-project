from django.urls import path
from .views import AdminOnlySpectacularAPIView, AdminOnlySwaggerView, AdminOnlyRedocView

urlpatterns = [
    path("schema/", AdminOnlySpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger/",
        AdminOnlySwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("docs/redoc/", AdminOnlyRedocView.as_view(url_name="schema"), name="redoc"),
]
