from django.contrib.auth import password_validation, authenticate

from rest_framework import serializers

from accounts.models import User


# =============================================================================
# UserSerializer
# =============================================================================
class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer
    """

    class Meta:
        model = User
        fields = '__all__'


# =============================================================================
# UserListSerializer
# =============================================================================
class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer data for list users
    """

    class Meta:
        model = User
        fields = [
            'id',
            'auth_token',
            'first_name',
            'last_name',
            'email',
            'auth_provider'
        ]
        read_only_fields = ('auth_token',)


# =============================================================================
# UserLoginSerializer
# =============================================================================
class UserLoginSerializer(serializers.ModelSerializer):
    """
    Serializer data for login
    """

    class Meta:
        model = User
        fields = [
            'id',
            'auth_token',
            'first_name',
            'last_name',
            'email',
            'auth_provider'
        ]
        read_only_fields = ('auth_token',)


# =============================================================================
# AuthenticateSerializer
# =============================================================================
class AuthenticateSerializer(UserSerializer):
    """
    AuthenticateSerializer for signup api
    """

    last4digits = serializers.SerializerMethodField()
    on_boarding_step = serializers.SerializerMethodField()
    transactions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'auth_token',
            'first_name',
            'last_name',
            'email',
            'auth_provider'
        ]
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}


# =============================================================================
# LoginSerializer
# =============================================================================
class LoginSerializer(serializers.ModelSerializer):
    """
    Login Serializer
    """

    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'tokens'
        ]

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        filtered_user_by_email = User.objects.filter(email=email)
        user = authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and \
                filtered_user_by_email[0].auth_provider != 'email':
            raise serializers.ValidationError({
                'message': f'Please continue your login using \
                    {filtered_user_by_email[0].auth_provider}.'
            })

        if user is None:
            raise serializers.ValidationError({
                'message': 'Invalid credentials, try again!'
            })

        if not user.is_active:
            raise serializers.ValidationError({
                'message': 'Account disabled, contact admin!'
            })

        return {
            'email': user.email,
            'tokens': user.tokens
        }


# =============================================================================
# SignUpSerializer
# =============================================================================
class SignUpSerializer(serializers.ModelSerializer):
    """
    Serializer for sign up API
    """

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]

    def validate_password(self, value):
        """
        Validate password field
        @param value: The value of password
        @return:
        """
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        """
        Create user with validated data
        @param validated_data: Validated data
        @return:
        """
        user = User.objects.create_user(**validated_data)
        return user
