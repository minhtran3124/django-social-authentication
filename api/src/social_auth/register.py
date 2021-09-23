from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from app.settings import SOCIAL_SECRET

from accounts.models import User


def register_social_user(provider: str, user_id: str, email: str, name: str):
    """
    Register social user
    @param provider:
    @param email:
    @return:
    """
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(email=email, password=SOCIAL_SECRET)
            return {
                # 'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()
            }
        else:
            raise AuthenticationFailed(
                detail=f'Please continue your login using '
                       f'{filtered_user_by_email[0].auth_provider}')
    else:
        user = {
            # 'username': email,
            'email': email,
            'password': SOCIAL_SECRET
        }

        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(email=email, password=SOCIAL_SECRET)

        return {
            'email': new_user.email,
            'tokens': new_user.tokens()
            # 'username': new_user.username,
        }
