from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing, name="listing"),
    path('addbase1', views.listing_addbase1, name="listing_addbase1"),
    path('pagination2', views.listing_2, name="listing_2"),
    path('addbase_ver2', views.listing_addbase_ver2, name="listing_addbase_ver2"),

]