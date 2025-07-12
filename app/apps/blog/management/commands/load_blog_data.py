import os
from django.conf import settings
from shared.base_loader import BaseDataLoaderCommand
from apps.blog.models import Category, Post
from django.utils.dateparse import parse_datetime


class Command(BaseDataLoaderCommand):
    help = "Load blog categories and posts from JSON"

    def __init__(self):
        super().__init__()
        self.data_file = os.path.join(
            settings.BASE_DIR, "apps", "blog", "data", "blog.json"
        )

    def load_items(self, data):
        categories = {}
        for category in data.get("categories", []):
            category_object, _ = Category.objects.update_or_create(
                slug=category["slug"], defaults={"name": category["name"]}
            )
            categories[category["slug"]] = category_object
            self.stdout.write(f"Category: {category_object.name}")

        for post in data.get("posts", []):
            category = categories.get(post["category_slug"])
            if not category:
                self.stderr.write(
                    f"Warning: Category '{post['category_slug']}' not found."
                )
                continue

            post_object, created = Post.objects.update_or_create(
                slug=post["slug"],
                defaults={
                    "title": post["title"],
                    "content": post["content"],
                    "category": category,
                    "publish_date": parse_datetime(post["publish_date"]),
                    "is_published": post.get("is_published", False),
                },
            )
            action = "Created" if created else "Updated"
            self.stdout.write(f"{action} post: {post_object.title}")
