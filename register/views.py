from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})
