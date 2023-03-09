from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_master = request.POST.get('is_master', False)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def zero(op=None): 
    if op: 
        return op(0) 
    else: 
        return 0 
def one(op=None): 
    if op: 
        return op(1) 
    else: 
        return 1 
def two(op=None): 
    if op: 
        return op(2) 
    else: 
        return 2 
def three(op=None): 
    if op: 
        return op(3) 
    else: 
        return 3 
def four(op=None): 
    if op: 
        return op(4) 
    else: 
        return 4 
def five(op=None): 
    if op: 
        return op(5) 
    else: 
        return 5 
def six(op=None): 
    if op: 
        return op(6) 
    else: 
        return 6 
def seven(op=None): 
    if op: 
        return op(7) 
    else: 
        return 7 
def eight(op=None): 
    if op: 
        return op(8) 
    else: 
        return 8 
def nine(op=None): 
    if op: 
        return op(9) 
    else: 
        return 9 
def plus(y): 
    return lambda x: x+y 
def minus(y): 
    return lambda x: x-y 
def times(y):


