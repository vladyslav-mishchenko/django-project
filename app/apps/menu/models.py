from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=16)
    slug = models.SlugField(
        unique=True, help_text="Unique code for the menu, e.g. 'main', 'aside'"
    )

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.menu.slug})"

    class Meta:
        ordering = ["order"]
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
