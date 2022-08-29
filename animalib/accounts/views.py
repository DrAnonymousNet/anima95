from audioop import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .tokens import account_activation_token  # to get token from tokens.py
from .forms import RegistrationForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm
from django.contrib import messages
from django.conf import settings
# I added these due to my issues with getting email
# from django.core.mail import EmailMessage
# from django.conf import settings


# Create your views here.


def accounts_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        print(registerForm.errors)
        print(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            # configure and set up email to be sent
            current_site = get_current_site(request)
            subject = 'Account Activation'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            user.email_user(subject=subject, message=message)
            # EmailMessage(subject=subject, message=message, body=message,
            #                 from_email=settings.EMAIL_FORM_USER,
            #                 to=[user.email])
            # email.send()
            # return HttpResponse('registered succesfully and activation sent') # could be linked to a template for users to access as Activation Success page. Try this instead if it will work return render(request, 'registration/nameoftemplate.html'), nameoftemplate could be check_activation_email
            return redirect('login')
    else:
        registerForm = RegistrationForm()
    return render(request, 'registration/register.html', {'form': registerForm})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect(reverse('login'))
        # return redirect('login')
    else:
        return render(request, 'registration/activation_invalid.html')


# def email(request):
#     return render(request, 'registration/email_notification.html')




class LoginView(View):

    def get(self, request):
        template = 'registration/login.html'
        login_form = UserLoginForm()
        context = {
            'form': login_form,
        }
        return render(request, template_name=template, context=context)

    def post(self, request):
        login_form = UserLoginForm(request.POST)
        print(login_form.errors, request.POST)
        if login_form.is_valid():
            print(request.POST)
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username, password)
            auth_user = authenticate(username=username, password=password)
            print(auth_user)
            if auth_user:
                print(auth_user)
                login(request, auth_user)   
                return redirect('animation:animation')
            return redirect(request.META.get('HTTP_REFERER'))

          
        #else:
        #    if login_form.errors:
        #        for field in login_form:
        #            for error in field.errors:
        #                messages.add_message(request, messages.ERROR, error)
        return redirect(request.META.get('HTTP_REFERER'))
