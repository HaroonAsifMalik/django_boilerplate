from django.urls import path

from accounts.views import SignUp

# password_reset_patterns = [
#     path("forgot/", PasswordReset.as_view(), name="password_forgot"),
#     path("forgot/confirm/", PasswordResetConfirm.as_view(), name="password_forgot_confirm"),
#     path("update/", ChangePassword.as_view(), name="password_update"),
# ]

urlpatterns = [
    path("sign-up/", SignUp.as_view(), name="signup"),
    # path("login/", Login.as_view(), name="login"),
    # path("logout/", LogOut.as_view(), name="logout"),
    # path("user/", UserProfile.as_view(), name="user_info"),
    # path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("password/", include(password_reset_patterns)),
]
