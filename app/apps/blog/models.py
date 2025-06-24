from django.db import models
from django.urls import reverse

# TODO: Refactor reserved slugs
RESERVED_SLUGS = ["posts", "categories", "admin", "login", "api", "static", "media"]


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("blog:category-detail", kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    content = models.TextField()
    excerpt = models.TextField(blank=True)

    publish_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="posts"
    )

    class Meta:
        ordering = ["-publish_date", "-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["is_published", "publish_date"]),
        ]

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"post_slug": self.slug})

    def __str__(self):
        return self.title
