from django.db import models
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from .validators import validate_isalpha, validate_phone_number
from datetime import datetime


class HwStoreUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(FIRST_NAME_MIN_LENGTH), validate_isalpha],
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(LAST_NAME_MIN_LENGTH), validate_isalpha],
        null=False,
        blank=False
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    profile_bio = models.TextField(
        null=True,
        blank=True
    )

    created_on = models.DateTimeField(
        auto_now_add=datetime.now()
    )


class PhoneNumbersUserModel(models.Model):
    phone = models.CharField(
        max_length=13,
        default=None,
        validators=[validate_phone_number, ]
    )

    user = models.ForeignKey(
        HwStoreUser,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(unique=True, null=True, blank=True)

    USERNAME_FIELD = 'slug'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.phone}-{self.id}")
        return super().save(*args, **kwargs)


