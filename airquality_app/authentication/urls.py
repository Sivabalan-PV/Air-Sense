from .views import RegistrationView,UserValidation
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from authentication.views import sign_up

urlpatterns = [
    path('register',RegistrationView.as_view(),name="register"),
    path('validate_user',csrf_exempt(UserValidation.as_view()),name="validate_user"),
     path('register/',sign_up , name='register'),

] 