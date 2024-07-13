from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('login/',LoginUser.as_view(),name="login"),
    path('logout/',logoutDef,name="logout"),
    path('register/',Register.as_view(),name="register"),
]
