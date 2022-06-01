from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LogInForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('kinamefilm:home')
    else:
        form = SignUpForm()
    return render(request, 'customuser/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home:home_page')
            else:
                form.add_error(None, 'Invalid email or password')
        else:
            form.add_error(None, 'Invalid input data')
    else:
        form = LogInForm()

    return render(request, 'customuser/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home:home_page')
