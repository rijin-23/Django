from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('cse',views.cse,name='cse'),
    path('etc',views.etc,name='etc'),
    path('mech',views.cse,name='mech'),
    path('civil',views.cse,name='civil'),
]
