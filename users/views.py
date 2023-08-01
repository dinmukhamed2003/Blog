
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm


def login_view(request):
    if request.method == 'GET':
        data = {
            'form': LoginForm,
            'user': get_user_from_request(request)

        }
        return render(request, 'users/login.html', context=data)
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error("username", "Bad request")
        data = {
            "form": form
        }
        return render(request, 'users/login.html', context=data)


def register_view(request):
    if request.method == 'GET':
        data = {
            'form': RegisterForm,
        }
        return render(request, 'users/register.html', context=data)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/login/')
            else:
                form.add_error('password1', 'Пароли не совпадают')
        return render(request, 'users/register.html', context={
            'form': form
        })