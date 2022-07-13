from django.urls import path
from auth_app.views import UserRegisterAPIViews, LoginView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('registration/', UserRegisterAPIViews.as_view(), name='user-registration'),
    path('loging/', LoginView.as_view(), name='user-login'),
    path('login/', obtain_auth_token, name='user-obtain_auth_token'),
]