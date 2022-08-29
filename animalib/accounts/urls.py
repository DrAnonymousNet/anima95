from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, PwdResetForm, PwdChangeForm, PwdResetConfirmForm

app_name = 'accounts'

urlpatterns = [
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html",
                                                                   form_class=PwdChangeForm), name='pwdforgot'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html",
                                                                 form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html', form_class=PwdResetConfirmForm), name="pwdresetconfirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
    path('register/', views.accounts_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/',
         views.activate, name='activate'),
    # path('register/email_notification/', views.email, name='email'),
]

