from django.contrib import admin
from django.urls import path,include
import Accounts
import Productapp
import Controlapp
import Api

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('Controlapp.urls')),
    path('',include('Accounts.urls')),
    path('',include('Productapp.urls')),
    path('api/',include('Api.urls')),
]


