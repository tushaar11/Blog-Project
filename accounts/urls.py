from django.urls import path

from . import views

urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('signout',views.signout,name="signout")
    ] 