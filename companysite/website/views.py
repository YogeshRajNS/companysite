from django.shortcuts import render, redirect
from .forms import formss

def home(request):
    form = formss()
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def contact_view(request):
    if request.method == 'POST':
        form = formss(request.POST)
        if form.is_valid():
            return redirect('submit')  # ✅ redirect to URL name
    else:
        form = formss()
    return render(request, 'home.html', {'form': form})

def submit_view(request):
    return render(request, 'submit.html')
