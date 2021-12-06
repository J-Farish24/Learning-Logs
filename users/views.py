from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    #Register a new users
    if request.method!= 'POST':
        #Display blank registration form
        form = UserCreationForm()
    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)
    #Username has the appropriate characters, the passwords match,
    #and the user isn't trying to do anything malicious in their submission
        if form.is_valid():
            new_user = form.save()
            #Log the user in and redirect to homepage
            login(request, new_user)
            return redirect('MainApp:index')

    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)