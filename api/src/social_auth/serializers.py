import os

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from app.settings import GOOGLE_OAUTH2_CLIENT_ID

from .google import Google
from .register import register_social_user


class GoogleSocialAuthSerializer(serializers.Serializer):
    """
    Google Social Authentication Serializer
    """
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = Google.validate(auth_token)
        try:
            user_data['sub']
        except err:
            raise serializers.ValidationError({
                'message': 'The token is invalid or expired. '
                           'Please login again.'
            })

        if user_data['aud'] != GOOGLE_OAUTH2_CLIENT_ID:
            raise AuthenticationFailed('Oops, Something went wrong. '
                                       'Please try again.')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(provider=provider,
                                    user_id=user_id,
                                    email=email, name=name)
