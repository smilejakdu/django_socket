from django.contrib   import admin
from django.conf.urls import include
from django.urls      import path

urlpatterns = [
    path('chat/' , include('chat.urls')),
]
