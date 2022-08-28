from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter New Password', 'id': 'psw-new', 'name': 'psw-new'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm New Password', 'id': 'psw-confirm-new', 'name': 'psw-confirm-new'}))

    def clean_password2(self):  # to ensure the two passwords are equal
        cd = self.cleaned_data
        if cd['new_password1'] != cd['new_password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['new_password2']


class UserLoginForm(AuthenticationForm):

    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'johndoe@gmail.com', 'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': '********',
            'id': 'password'
        }
    ))


class PwdChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Old Password', 'id': 'psw-old', 'name': 'psw-old'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter New Password', 'id': 'psw-new', 'name': 'psw-new'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm New Password', 'id': 'psw-confirm-new', 'name': 'psw-confirm-new'}))

    def clean_password1(self):
        old_password = self.cleaned_data['password']
        test = User.objects.filter(old_password=old_password)
        if not test:
            raise forms.ValidationError(
                'Password is not recognized')
        return old_password

    def clean_password2(self):  # to ensure the two passwords are equal
        cd = self.cleaned_data
        if cd['new_password1'] != cd['new_password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['new_password2']


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.EmailInput(
        attrs={'placeholder': 'Enter email', 'id': 'email', 'name': 'email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError(
                'Unfortunately, email address is not recognized')  # you might do something more secure than this because this will give some people the knowledge of emails that exist or not in database
        return email


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',)

    # method to check if username already exists in database, not necessary if your username in Login Page will be an Emailfield
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_password2(self):  # to ensure the two passwords are equal
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):  # to check if email is unique in database
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, this is already taken')
        return email

    def __init__(self, *args, **kwargs):  # adding attributes from our style to the fields
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'John Doe', 'name': 'name', 'id': 'name'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'johndoe@gmail.com', 'name': 'email', 'id': 'email'})
        self.fields['password'].widget.attrs.update(
            {'placeholder': '********', 'name': 'password', 'id': 'password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'label', 'placeholder': 'Repeat Password'})
