from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [
    path('signup',views.signupview,name='signup'),
    path('check_username_exist',views.check_username_existview,name='check_username_exist'),
    path('login',views.loginview,name='login'),
    path('logout',views.logoutview,name='logout'),
    re_path(r'^(.*)signup/$',views.signupview,name='signup'),
    re_path(r'^(.*)login/$',views.loginview,name='login'),
    re_path(r'^(.*)logout/$',views.logoutview,name='logout'),
    re_path(r'^(.*)verification/$',views.verificationview,name='verification'),
    path('verification/',views.verificationview,name='verification'),
    path('signup/resend-otp/',views.resend_otp,name='resend-otp'  ),
    path('signup/resend-otp/verification/',views.verificationview,name='verification'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'), 
    path('subscribe',views.subscribeview,name="subscribe"),
    path('contact/',views.contactview,name='contact'),
    path('change_password',views.changepasswordview,name='change_password')
    ]