from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response
from signup.forms import SignUpForm

def Signup(request):
        if request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                        user = form.save()
                        user.refresh_from_db()  # load the profile instance created by the signal
                        user.profile.birth_date = form.cleaned_data.get('birth_date')
                        user.save()
                        raw_password = form.cleaned_data.get('password1')
                        user = authenticate(username=user.username, password=raw_password)
                        login(request, user)
                        return redirect('/thanks/')
        else:
                form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

def thanks(requiest):
	return render_to_response("thanks.html")
		