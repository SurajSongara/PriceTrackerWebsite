from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.aboutview,name='about'),
    path('mail/',views.mailview,name='mail'),
    path('codes/',views.codesview,name='codes'),
    path('icons/',views.iconsview,name='icons'),
    path('star/',views.starview,name='star'),
    path('faq/',views.faqview,name='faq'),
]



