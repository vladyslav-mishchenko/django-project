from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Form Message"
        verbose_name_plural = "Contact Form Messages"

    def __str__(self):
        return f"{self.name} ({self.email})"
