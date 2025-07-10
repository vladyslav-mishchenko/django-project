# Abstract base loader classes for data import

# shared/base_loader.py

import os
from django.core.management.base import BaseCommand, CommandError


class BaseDataLoaderCommand(BaseCommand):
    data_file = None  # Should be overridden in subclasses

    def handle(self, *args, **options):
        if not self.data_file:
            raise CommandError("No data file specified.")

        self.stdout.write(self.style.NOTICE(f"Loading data from {self.data_file}..."))
        data = self.load_data(self.data_file)
        self.load_items(data)
        self.stdout.write(self.style.SUCCESS("Data loaded successfully."))

    def load_data(self, path):
        import json

        if not os.path.exists(path):
            raise CommandError(f"File not found: {path}")
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def load_items(self, data):
        raise NotImplementedError("Subclasses must implement load_items()")
