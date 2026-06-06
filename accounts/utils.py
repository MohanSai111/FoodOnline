
from .models import User


def detectUser(user):
    """Return the name or path to redirect the given user to.

    Uses `User.VENDOR` and `User.CUSTOMER` constants and always returns
    a non-None string as a fallback.
    """
    if user is None:
        return 'login'

    if user.role == User.VENDOR:
        return 'vendordashboard'
    if user.role == User.CUSTOMER:
        return 'custdashboard'
    if getattr(user, 'is_superadmin', False):
        return '/admin'

    # fallback to account home
    return 'myAccount'
