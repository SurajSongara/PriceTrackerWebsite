from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import CustomUser, Feedback, Subscription
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from Productapp.models import Cart
import random
import json
import os
import re


@csrf_exempt
def check_username_existview(request):
    Email = request.POST.get("username")
    user_obj = CustomUser.objects.filter(email=Email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def signupview(request, x=None):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        password1 = request.POST['Password']
        password2 = request.POST['Confirm_password']

        user = CustomUser.objects.filter(email=email).first()
        if user:
            if not user.is_active:
                user.delete()


        if not re.match(r"[^@]+@[^@]+\.[^@]+", email) :
            messages.warning(request, "Invalid email address")
            return redirect('home')


        user_obj = CustomUser.objects.filter(email=email).exists()
        if not user_obj:
            if password1 == password2:
                password1 = make_password(password1)
                user = CustomUser.objects.create(
                    first_name=name, email=email, password=password1)
                user.is_active = False
                user.save()
                otp = str(random.randint(100000, 999999))
                user.set_otp(otp)
                msg = "Your one time password for account verification is : " + otp
                sub = "One time password Price Tracker"
                send_mail(subject=sub, message=msg,
                          from_email=settings.DEFAULT_FROM_EMAIL,
                          recipient_list=[email],
                          fail_silently=False)

                return render(request, 'verification.html', {'user': user})

            else:
                messages.warning(request, "Passwords did not matched ")
                return redirect('home')
        else:
            messages.warning(request, "Please use a different email id ")
            return redirect('home')

    else:
        return HttpResponse('404 not found')


@csrf_exempt
def loginview(request, x=None):
    if request.method == "POST":
        loginusername = request.POST['Email']
        loginpassword = request.POST['Password']
        usr = authenticate(request, email=loginusername,
                           password=loginpassword)
        if usr is not None:
            login(request, usr)
            messages.success(
                request, " Congratulations you are successfully logged in")
        else:
            messages.error(request, " Invalid login credentials ")
        return redirect('home')
    else:
        return redirect('home')


def logoutview(request, x=None):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('home')


@csrf_exempt
def verificationview(request,x=None):
    if request.method == 'POST':
        email = request.POST.get('Email')
        current_otp = request.POST.get('otp')
        user= CustomUser.objects.filter(email=email).first()
        if user.otp == current_otp:
            user.is_active = True
            user.save()
            messages.success(request, 'You are logged in successfully')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'INVALID ONE TIME PASSWORD !')
            return render(request, 'verification.html', {'user': user})




@csrf_exempt
def resend_otp(request):
    email = request.POST.get('email')
    user = CustomUser.objects.filter(email=email).first()
    otp = str(random.randint(100000, 999999))
    user.set_otp(otp)
    msg = "Your one time password for account verification is : " + otp
    sub = "One time password Price Tracker"
    send_mail(subject=sub, message=msg,
              from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=[email],
              fail_silently=False)
    return HttpResponse(otp)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = CustomUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "mail_text/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL,
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
            else:
                messages.error(
                    request, "There is no user associated with this email id")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form": password_reset_form})


def subscribeview(request):
    if request.method == 'POST':
        Email = request.POST.get('mail_id')
        usr = Subscription(Email=Email)
        usr.save()
        subject = "Thank you for subscribing us "
        email_template_name = "mail_text/subsrcibe_mail.txt"
        body = render_to_string(email_template_name)
        try:
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                      [Email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found !')
        return HttpResponse('You are subscribed !')


@csrf_exempt
def contactview(request):
    Name = request.POST.get('Name')
    Email = request.POST.get('Email')
    Telephone = request.POST.get('Telephone')
    Mesasge = request.POST.get('Message')
    feedback = Feedback(Name=Name, Email=Email,
                        Phone=Telephone, Message=Mesasge)
    feedback.save()
    subject = "Thank you for contacting"
    email_template_name = "mail_text/contact_mail.txt"
    body = render_to_string(email_template_name, {'name': Name})
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                  [Email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return redirect("mail")

