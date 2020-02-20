from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def logout(request):

    auth.logout(request)
    messages.success(request, 'Du är nu utloggad')
    return redirect(reverse('index'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'Du är nu inloggad!')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Du har anget fel lösenord eller användarnamn!')    
    else:
        login_form = UserLoginForm()    
    return render(request, 'login.html', {'login_form':login_form})    


def registration(request):
    registration_form = UserRegistrationForm()


    return render(request,'registration.html', {'registration_form': registration_form})