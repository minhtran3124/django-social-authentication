from django.contrib.auth import authenticate

from rest_framework.decorators import action
from rest_framework import serializers

from drf_core import apis, apidoc

from app.pagination import BasePaginationCommon
# from app.pagination import StandardResultsSetPagination

from accounts.models import User
from accounts.filters import UserFiltering
from accounts.serializers import (
    AuthenticateSerializer,
    SignUpSerializer,
    UserListSerializer,
    UserLoginSerializer,
)
from accounts.permission import IsAdmin


# =============================================================================
# LoginView
# =============================================================================
class LoginView(apis.BaseFunctionView):
    """
    Single function view for login API
    """

    resource_name = ''

    @apidoc.swagger_auto_schema(
        responses={200: 'OK'},
        manual_parameters=[
            apidoc.Parameter(
                'email',
                apidoc.IN_QUERY,
                description='Email',
                type=apidoc.TYPE_STRING,
                required=True,
            ),
            apidoc.Parameter(
                'password',
                apidoc.IN_QUERY,
                description='Password',
                type=apidoc.TYPE_STRING,
                format=apidoc.FORMAT_PASSWORD,
                required=True,
            )
        ]
    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            return self.bad_request(
                message='Can not authenticate user',
                code=400
            )

        # get user data.
        user_data = UserLoginSerializer(user)

        return self.create_response(user_data.data)


# =============================================================================
# LogoutView
# =============================================================================
class LogoutView(apis.BaseFunctionView):
    """
    Single function view for logout API.
    """

    @apis.authentication_classes(
        (apis.SessionAuthentication, apis.TokenAuthentication)
    )
    @apis.permission_classes((apis.IsAuthenticated,))
    def get(self, request, format=None):
        """
        Log out API
        """
        if not request.user.pk:
            return self.bad_request(message='You are not logged in', code=400)

        return self.create_response()


# =============================================================================
# SignUpView
# =============================================================================
class SignUpView(apis.BaseFunctionView):
    """
    Single function view for signup API.
    """
    resource_name = 'signup'

    def post(self, request):
        """
        POST /api/v1/signup/
        API for user create new account
        """
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # create new account
        user = serializer.save()

        # serializer for response data
        response = AuthenticateSerializer(user).data
        return self.create_response(response)


# =============================================================================
# PasswordForgotView
# =============================================================================
class PasswordForgotView(apis.BaseFunctionView):
    """
    Single function view for return message when admin forgot password
    """
    resource_name = 'password-forgot'

    def post(self, request):
        """
        POST /password-forgot/
        API for generate link reset password
        """
        pass


# =============================================================================
# LoginView
# =============================================================================
class PasswordResetView(apis.BaseFunctionView):
    """
    Single function view for admin password reset
    """
    resource_name = 'password-reset'

    def post(self, request, *args, **kwargs):
        """
        POST /password-reset/
        API for generate link reset password
        """
        pass


# =============================================================================
# PasswordSetView
# =============================================================================
class PasswordSetView(apis.BaseFunctionView):
    """
    Single function for view set new password for user
    """
    resource_name = 'password-set'

    def post(self, request, *args, **kwargs):
        """
        POST /password-set/
        API for generate link reset password
        """
        pass


# =============================================================================
# UserViewSet
# =============================================================================
class UserViewSet(apis.BaseViewSet):
    """
    User API ViewSet
    """

    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserListSerializer
    pagination_class = BasePaginationCommon
    filter_class = UserFiltering
    permission_classes = [IsAdmin]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', ]
    ordering_fields = '__all__'
    search_fields = []

    resource_name = 'users'


# define all routers
apps = [
    UserViewSet,
]
