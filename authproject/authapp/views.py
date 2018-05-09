from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from authapp.forms.sign_up import SignUpForm
import sys
# Create your views here.


def sign_up(request):

    if(request.method == "POST"):
        sign_up_form = SignUpForm(request.POST)
        if(sign_up_form.is_valid):
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user = User()
            print(type(request.POST.get('email1')))
            print(request.POST.get('email1'))
            sys.exit(0)
            user.set_password(password)
            user.username = username
            user.email = email
            user.save()

    else:
        sign_up_form = SignUpForm()
    context = {
        'form': sign_up_form
    }
    return render(request, 'authapp/sign_up.html', context)
