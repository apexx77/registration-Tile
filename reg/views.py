from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request) :
    return render(request, 'home.html')
def registrationpage(request) :
    return render(request, 'index.html')
def final(request) :
    if request.method == 'POST' :
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        username = request.POST['user-name']
        email = request.POST['your-email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
        user.save();

        return render(request, 'ty.html')