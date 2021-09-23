import os

# ----------------------------------------------------------------------------
# Definition auth provider
# ----------------------------------------------------------------------------
AUTH_PROVIDERS = {
    'email': 'email',
    'google': 'google',
    'facebook': 'facebook',
    'twitter': 'twitter',
}

# ----------------------------------------------------------------------------
# The url reset password
# ----------------------------------------------------------------------------
RESET_PASSWORD_URL = '/reset-password'
SET_PASSWORD_URL = '/set-password'

# ----------------------------------------------------------------------------
# The default admin email
# ----------------------------------------------------------------------------
ADMIN_DEFAULT_EMAIL = os.environ.get('ADMIN_DEFAULT_EMAIL')

# ----------------------------------------------------------------------------
# define password message for admin
# ----------------------------------------------------------------------------
PASSWORD_MESSAGE = {
    'FORGOT': 'A reset Password link has been sent to',
    'RESET_NOT_MATCH': 'Your password and confirmation password do not match.',
    'UID_NOT_VALID': 'The uidb64 is not valid.',
    'TOKEN_NOT_VALID': 'The token is not valid.',
    'LINK_NOT_VALID': 'Your reset password link is not valid.',
    'PASSWORD_IN_VALID': 'Password requires a minimum length of 8 characters'
                         ' with at least one numerical digit and one letter.'
}
