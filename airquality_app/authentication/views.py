from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm  # Assuming you've created a custom form
from AQMapp.models import user
def sign_up(request):
      if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user against the database
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is valid, log them in
            login(request, user)
            # Redirect to the dashboard or any other desired page
            return redirect('dashboard')
        else:
            # Invalid credentials, show an error message
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'authentication/register.html', {'error_message': error_message})
    
      return render(request, 'authentication/register.html')



class UserValidation(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']
        user = authenticate(request, username=username)
        if user is not None:
            return JsonResponse({'username_error':'username doesnt Exist'},status=409)
        return JsonResponse({'username_valid':True})
    

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    def post(self,request):
        return render(request,'authentication/register.html')
    
    