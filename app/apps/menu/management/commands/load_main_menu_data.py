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
        # data is a dict representing one menu
        menu, created = Menu.objects.update_or_create(
            slug=data["slug"], defaults={"name": data["name"]}
        )
        self.stdout.write(f"{'Created' if created else 'Updated'} menu: {menu.name}")

        # Clear existing items (optional)
        menu.items.all().delete()

        # Add items in order
        items = data.get("items", [])
        for item_data in items:
            menu_item = MenuItem.objects.create(
                menu=menu,
                title=item_data["title"],
                url=item_data["url"],
                order=item_data.get("order", 0),
            )
            self.stdout.write(f"  Added menu item: {menu_item.title}")
