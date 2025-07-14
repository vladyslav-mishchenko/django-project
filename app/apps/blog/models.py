import random
import string

from django.db import models
from django.urls import reverse
from django.utils.timezone import now

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


def generate_unique_post_id():
    prefix = "POST"
    date_part = now().strftime("%Y-%m")
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{date_part}-{random_part}"


def post_image_upload_path(instance, filename):
    post_id = instance.post_id or "unassigned"
    ext = filename.split(".")[-1]
    return f"blog/posts/{post_id}/preview.{ext}"


class Post(models.Model):
    post_id = models.CharField(max_length=20, unique=True, editable=False, null=True)

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    excerpt = models.TextField(blank=True)
    preview_image = models.ImageField(
        upload_to=post_image_upload_path, null=True, blank=True
    )

    content = models.TextField()

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

    def save(self, *args, **kwargs):
        if not self.post_id:
            while True:
                candidate = generate_unique_post_id()
                if not Post.objects.filter(post_id=candidate).exists():
                    self.post_id = candidate
                    break

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"post_slug": self.slug})

    def __str__(self):
        return self.title
