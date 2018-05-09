from django.shortcuts import render
from django.http import HttpResponse
from authapp.forms.sign_up import SignUpForm
# Create your views here.


def sign_up(request):

    if(request.method == "POST"):
        sign_up_form = SignUpForm(request.POST)
        if(sign_up_form.is_valid):
            sign_up_form.save()

    else:
        sign_up_form = SignUpForm()
    context = {
        'form': sign_up_form
    }
    return render(request, 'authapp/sign_up.html', context)
