import re
import secrets
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from stdnum.pl import pesel


# Creating the validator checks PESEL id


def validate_patient_pesel(value):
    # First check if value is not empty or if is not long enough
    is_valid = pesel.is_valid(value)
    if not is_valid:
        raise ValidationError(
            _('PESEL jest nieprawidłowy.'), code='invalid')

    return value


# Validator for zip code

def validate_zip_code(value):
        # Validate the zip code
    match = re.search(r'^\d{2}\d{3}$', value)
    if not match:
        raise ValidationError(
            _('Kod pocztowy jest nieprawidłowy.'), code='invalid')

    return value


# Get random sequence for Visit ID
def get_random_secret():
    return secrets.token_urlsafe(9)
