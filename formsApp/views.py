from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import HTML_storing_form

def homepage_view(request):
    return render(request, "homepage.html")

def login_view(request):
    error_message = ""
    if request.method == "POST":
        # Handle login form submission
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication successful
            login(request, user)
            return redirect(
                "user_dashboard"
            )  # Redirect to the profile page after successful login
        else:
            # User authentication failed
            error_message = "Invalid username or password"
            return render(request, "login.html", {"error_message": error_message})
    else:
        # Check if there is an error message in the session
        if "error_message" in request.session:
            error_message = request.session.pop(
                "error_message"
            )  # Retrieve and remove the error message from the session

    return render(
        request,
        "login.html",
    )

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


@login_required(login_url="login")
def user_dashboard(request):
    user = request.user
    user_data = list(HTML_storing_form.objects.all().filter(user=user).values())
    context = {
        "user": user,
        "user_data": user_data
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="login")
def form_builder_view(request):
    # https://github.com/sumbria/bootstrap-form-builder
    if request.method == "POST":
        username = request.user
        form_name = request.POST.get("form_name")
        form_html = request.POST.get("html_form")
        custom_form = HTML_storing_form(user = username, form_name = form_name, form_html = form_html)
        custom_form.save()
    return render(request, "form_builder.html")
