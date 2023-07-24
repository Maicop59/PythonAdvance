from django.urls import path
from . import views

urlpatterns = [
    path('', views.regform, name="regform" ),
]