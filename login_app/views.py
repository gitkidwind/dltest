from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ChildUser
from .forms import CustomUserCreationForm , CustomUserChangeForm , CustomPasswordChangeForm ,CustomUserLoginForm ,ChildUserForm

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            # ログイン後の処理を実行
            return redirect('home_app:home_page')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_app:login_view')

@login_required
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('home_app:home_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login_app/register.html', {'form': form})


@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_app:login_view')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'login_app/password_change.html', {'form': form})


@login_required
def user_profile_edit_view(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('login_app:user_profile_view')
        else:
            messages.error(request, 'There was an error updating your profile. Please try again.')
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'login_app/user_profile_edit.html', {'form': form})


@login_required
def user_profile_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'login_app/user_profile.html', context)

@login_required
def childuser_list(request):
    childusers = ChildUser.objects.all()
    return render(request, 'login_app/childuser_list.html', {'childusers': childusers})
@login_required
def childuser_new(request):
    if request.method == 'POST':
        form = ChildUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_app:childuser_list')
    else:
        form = ChildUserForm()
    return render(request, 'login_app/childuser_new.html', {'form': form})