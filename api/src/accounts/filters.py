from drf_core.filtering import filters, BaseFiltering

from accounts.models import User


# =============================================================================
# UserCampaign
# =============================================================================
class UserFiltering(BaseFiltering):
    """
    UserCampaign Filtering
    """

    class Meta:
        model = User
        exclude = []
