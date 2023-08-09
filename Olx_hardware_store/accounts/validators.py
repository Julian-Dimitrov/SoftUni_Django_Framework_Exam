from django.core.exceptions import ValidationError
import re


def validate_isalpha(name):
    if not name.isalpha():
        raise ValidationError('This box must consist only of letters!')


def validate_phone_number(phone_number):
    phone_number_pattern = re.compile(r'^((\+?\d{3})|\d{1})(\d{9})$')

    if not phone_number_pattern.match(phone_number):
        raise ValidationError('Invalid phone number format!')
