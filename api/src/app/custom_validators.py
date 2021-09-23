import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from app.constants import ERROR_MESSAGE


class CustomPasswordValidator:
    @staticmethod
    def validate(self, password, user=None):
        if len(password) <= 7:
            raise ValidationError(
                _(ERROR_MESSAGE['PASSWORD_IN_VALID']),
                code='password_no_length',
            )

        if not len(re.findall('\d', password)) >= 1:
            raise ValidationError(
                _(ERROR_MESSAGE['PASSWORD_IN_VALID']),
                code='password_no_number'
            )

        if not re.findall('[a-z]|[A-Z]', password):
            raise ValidationError(
                _(ERROR_MESSAGE['PASSWORD_IN_VALID']),
                code='password_no_letter',
            )
