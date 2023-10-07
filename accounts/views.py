from django.shortcuts import render, redirect
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
def sign_in(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user=authenticate(request, username=username, password=password)
            
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, 'Login request was successfull')
                return redirect('list')
        messages.error(request, 'Invalid username or password')
    form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})

def sign_out(request):
    logout(request)
    messages.success(request,'Logout request was successfull')
    return redirect('login')

def sign_up(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            # Profile.objects.create(user=user)
            return render(request,'accounts/register_done.html',{'user':user})
        
    else:
        form=UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})


def edit(request):
    if request.method == 'POST':
        user_form=UserEditForm(instance=request.user, data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and  profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('list')
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)
    return render(request,'accounts/profile.html',{'user_form':user_form,'profile_form':profile_form})