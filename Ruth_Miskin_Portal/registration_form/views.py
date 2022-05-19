from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'forms/index.html')

def register(request):
    print('hi')
    if request.method == 'POST':
        print('there')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        DoB = request.POST['birthday']

        user = User.objects.create_user(fname = fname, lname = lname, email = email)
        user.DoB = DoB
        user.save()
        print('user created')
        return redirect('login')
    else:
        return render(request, 'forms/register.html')

def login(request):
    return render(request, 'forms/login.html')

#def logout(request):
    #pass

