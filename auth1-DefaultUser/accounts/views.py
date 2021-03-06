from django.shortcuts import render, redirect
from .forms import HiddenUserCreationForm
from django.contrib.auth import login, authenticate

def index(request):
    context = {'user':request.user}
    return render(request, 'accounts/index.html', context)

def register(request):
    if request.method == 'POST':
        form = HiddenUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:index')
    else:
        form = HiddenUserCreationForm()
    
    context = {'form':form}
    return render(request, 'accounts/register.html', context)
