from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import PersonForm
from django.http import JsonResponse
import json
from .models import Branch






def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']  

        if password == confirm_password:
            if User.objects.filter(username=username).exists():  
                messages.info(request, "Username is already taken")
                return redirect('register')

            else:
                
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "User registered successfully!")
                return redirect('login')

        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    return render(request, "register.html")



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return redirect('login')
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('button')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')





def button(request):
    return render(request, 'btn.html')





def Customer_forms(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Application accepted')
    else:  
        form = PersonForm()
    return render(request, "form.html", {"form": form})


def branches(request):
    data = json.loads(request.body)
    branches = Branch.objects.filter(district__id=data['user_id'])
    print(branches)
    return JsonResponse(list(branches.values("id", "name")), safe=False)





def logout(request):
    auth.logout(request)
    return redirect('/')



