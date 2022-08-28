from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    # the default value for password reset token is 7 Days, you can change or reduce it in settings.py file, Check Django documentation, maybe this is the parameter to set it password_reset_timeout_days
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp) +
            text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()
