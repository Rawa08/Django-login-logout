from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def logout(request):

    auth.logout(request)
    messages.success(request, 'Du är nu utloggad')
    return redirect(reverse('index'))