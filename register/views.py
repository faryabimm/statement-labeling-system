from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthenticationForm()
            return render(request, 'registration/login.html', context={
                "form": form,
                "notify": {
                    "type": "success",
                    "title": "Success",
                    "message": "Registration successful."
                }
            })
        else:
            form = UserCreationForm()
            return render(request, 'register/register.html', context={
                "form": form,
                "notify": {
                    "type": "danger",
                    "title": "Failed",
                    "message": "Registration Failed."
                }
            })
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})
