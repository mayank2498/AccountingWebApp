from django.shortcuts import render,redirect
from django.conf.urls import url
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_user(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    print('before redirect')
                    return redirect('http://127.0.0.1:8000/firm/firm_login')
                else:
                    return render(request,'login/login_admin.html',{'error_message':'Your account has been disabled'})
            else:
                return render(request,'login/login_admin.html',{'error_message':'Invalid Username or Password. Login Again'})
        else:
            return render(request,'login/login_admin.html')
    else:
        return redirect('http://127.0.0.1:8000/firm/firm_login')

def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/login/')