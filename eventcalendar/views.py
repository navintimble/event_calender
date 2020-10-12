from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from calendarapp.forms import SignupForm


def signup(request):
    forms = SignupForm()
    if request.method == 'POST':
        forms = SignupForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('calendarapp:calendar')
            else:
                return render(request, 'signup.html', {'error': "Username and password not match"})

    context = {'form': forms}
    return render(request, 'signup.html', context)


def user_logout(request):
    logout(request)
    return redirect('signup')
