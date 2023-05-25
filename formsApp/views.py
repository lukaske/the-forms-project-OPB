from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    error_message = ""
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication successful
            login(request, user)
            return redirect('user_dashboard')  # Redirect to the profile page after successful login
        else:
            # User authentication failed
            error_message = "Invalid username or password"  # Customize your error message as needed
            return render(request, 'homepage.html', {'error_message': error_message})
    else:
        # Check if there is an error message in the session
        if 'error_message' in request.session:
            error_message = request.session.pop('error_message')  # Retrieve and remove the error message from the session

    return render(request, 'homepage.html', )

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_dashboard(request):
    user = request.user
    # Retrieve user-specific data or perform any necessary processing
    context = {
        'user': user,
        # Add more context data as needed
    }
    return render(request, 'dashboard.html', context)

def form_builder_view(request):
    return render(request, 'form_builder/form_builder.html')