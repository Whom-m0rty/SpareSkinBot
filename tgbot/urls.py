from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('notice_status/', views.notice_status, name='index'),
]
