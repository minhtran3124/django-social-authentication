from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings

from accounts.tokens import account_activation_token
from accounts.constants import RESET_PASSWORD_URL


def generate_reset_password_link(instance):
    """
    Generate reset password link
    @param instance:
    @return:
    """
    uid = urlsafe_base64_encode(force_bytes(instance.pk))
    token = account_activation_token.make_token(instance)
    domain = settings.WEB_APPLICATION_DOMAIN

    return f'{domain}{RESET_PASSWORD_URL}/{uid}/{token}'


def get_user_by_uidb64(user_model, uidb64):
    """
    Get user by uidb64
    @param user_model: User model
    @param uidb64: uid string code
    @return:
    """
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = user_model.objects.get(pk=uid)

    return user
