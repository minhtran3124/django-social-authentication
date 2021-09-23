import os


# Google Credentials
GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_ACCESS_TOKEN_REVOKE_URL = 'https://oauth2.googleapis.com/revoke'
GOOGLE_OAUTH2_V4_TOKEN_URL = 'https://www.googleapis.com/oauth2/v4/token'
GOOGLE_TOKEN_URI = 'https://oauth2.googleapis.com/token'

GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')
SOCIAL_SECRET = os.environ.get('SOCIAL_SECRET')

# Scopes APIs
YOUTUBE_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly'
]

ADSENSE_SCOPES = [
    'https://www.googleapis.com/auth/adsense.readonly'
]

API_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/adsense.readonly'
]
