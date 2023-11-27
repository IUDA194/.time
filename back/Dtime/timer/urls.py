from django.contrib import admin
from django.urls import path
from timer.views import timer_ssesion
urlpatterns = [
    path("timer/", timer_ssesion().route)
]
