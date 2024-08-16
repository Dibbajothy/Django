from django.shortcuts import render, redirect
from django.contrib import messages
from basicapp.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout






def index(request):
    return render(request, 'basicapp/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")




@login_required
def user_logout(request):
    logout(request)
    return redirect('index')




def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            messages.success(request, "Registration successful!")
            return redirect('user_login')  # Redirect to the index page after successful registration
        else:
            messages.error(request, user_form.errors)
            messages.error(request, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basicapp/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    })




def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            print("Someone tried to login and failed!")
            print("Username : {} and Password {}".format(username, password))

    return render(request, 'basicapp/login.html')
