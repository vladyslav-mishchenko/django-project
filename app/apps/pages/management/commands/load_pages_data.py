import os
from django.conf import settings
from shared.base_loader import BaseDataLoaderCommand
from apps.pages.models import Page


class Command(BaseDataLoaderCommand):
    help = "Load initial page data from JSON"

    def __init__(self):
        super().__init__()
        self.data_file = os.path.join(
            settings.BASE_DIR, "apps", "pages", "data", "pages.json"
        )

    def load_items(self, data):
        for item in data:
            page, created = Page.objects.update_or_create(
                slug=item["slug"],
                defaults={"title": item["title"], "content": item["content"]},
            )
            action = "Created" if created else "Updated"
            self.stdout.write(f"{action} page: {page.title}")
