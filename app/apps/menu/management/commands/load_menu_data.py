# apps/menu/management/commands/load_menu_data.py

import os
from django.conf import settings
from shared.base_loader import BaseDataLoaderCommand
from apps.menu.models import Menu, MenuItem


class Command(BaseDataLoaderCommand):
    help = "Load initial menu data from JSON"

    def __init__(self):
        super().__init__()
        self.data_file = os.path.join(
            settings.BASE_DIR, "apps", "menu", "data", "main-menu.json"
        )

    def load_items(self, data):
        menus = {}

        for menu in data.get("menus", []):
            menu_object, _ = Menu.objects.update_or_create(
                slug=menu["slug"], defaults={"name": menu["name"]}
            )
            menus[menu["slug"]] = menu_object
            self.stdout.write(f"Category: {menu_object.name}")

        for item in data.get("items", []):
            menu = menus.get(item["menu_slug"])
            if not menu:
                self.stderr.write(f"Warning: Menu '{item['menu_slug']}' not found.")
                continue

            menu_item_object, created = MenuItem.objects.update_or_create(
                url=item["url"],
                defaults={
                    "title": item["title"],
                    "url": item["url"],
                    "order": item["order"],
                    "menu": menu,
                },
            )
            action = "Created" if created else "Updated"
            self.stdout.write(f"{action} menu: {menu_item_object.title}")
