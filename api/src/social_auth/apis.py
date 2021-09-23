from drf_core import apis

from social_auth.serializers import GoogleSocialAuthSerializer


class GoogleSocialAuthView(apis.BaseFunctionView):
    """
    Google Authentication View
    """
    resource_name = 'google'

    def post(self, request):
        """
        POST with "auth_token"
        Send an id token as from google to get user information
        """
        serializer = GoogleSocialAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data['auth_token']

        return self.create_response(data)


class FacebookSocialAuthView(apis.BaseFunctionView):
    """
    Facebook Authentication View
    """
    resource_name = 'facebook'

    def post(self, request):
        pass


class TwitterSocialAuthView(apis.BaseFunctionView):
    """
    Twitter Authentication View
    """
    resource_name = 'twitter'

    def post(self, request):
        pass
