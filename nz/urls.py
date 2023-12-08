from nz.views import *

from django.urls import path

app_name='tbr'

urlpatterns=[
    path('philips/',philips,name='philips')
]