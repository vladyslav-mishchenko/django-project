from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.post_list, name="post-list"),
    path("categories/", views.category_list, name="category-list"),
    path(
        "categories/<slug:category_slug>/",
        views.category_detail,
        name="category-detail",
    ),
    path("posts/<slug:post_slug>/", views.post_detail, name="post-detail"),
]
