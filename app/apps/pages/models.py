from django.db import models

# from django.urls import reverse

# TODO: Refactor reserved slugs
RESERVED_SLUGS = ["posts", "categories", "admin", "login", "api", "static", "media"]


class Page(models.Model):
    title = models.CharField(max_length=32, unique=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=32, unique=True, blank=True)
    template = models.CharField(
        max_length=16,
        default="default",
        verbose_name="Template",
        help_text="Template name without extension, e.g. 'about' or 'contact'",
    )
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Page id={self.id} title={self.title!r}"
