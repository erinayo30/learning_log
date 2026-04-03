from django.shortcuts import render, redirect
from django.contrib.auth import login
# from django.contrib.auth.forms import CustomUserCreationForm
from learning_logs.forms import CustomUserCreationForm
# Create your views here.

def register(request):
    """Register a new user in the system"""
    if request.method != 'POST':
#         Display Blank registration form
        form = CustomUserCreationForm()
    else:
# process complete form
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user= form.save()
#             log the user in and then redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')
#     Display blank or invalid form
    context = { 'form': form}
    return render(request, 'accounts/register.html', context)
