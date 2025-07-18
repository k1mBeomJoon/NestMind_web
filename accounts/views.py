from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from django.contrib.auth import views as auth_views
from django.http import HttpRequest

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_choice(request: HttpRequest):
    if request.GET.get('real') == '1':
        return auth_views.LoginView.as_view(template_name='accounts/login_real.html')(request)
    return render(request, 'accounts/login.html')