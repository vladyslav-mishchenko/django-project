from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("<slug:page_slug>/", views.page_detail, name="page-detail"),
]
