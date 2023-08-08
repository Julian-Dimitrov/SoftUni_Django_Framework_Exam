from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from Olx_hardware_store.settings import AUTH_USER_MODEL

UserModel = get_user_model()


class Tool(models.Model):  # napravi created_on
    name = models.CharField(
        max_length=50
    )

    tool_photo = models.URLField()

    description = models.TextField(
        max_length=200
    )

    tool_country = models.CharField(
        max_length=30
    )

    tool_city = models.CharField(
        max_length=50
    )

    tool_price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'slug'
    REQUIRED_FIELDS = []

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)
