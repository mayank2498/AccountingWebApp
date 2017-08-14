from django.shortcuts import render,redirect
from django.conf.urls import url
from django.contrib.auth import authenticate,login,logout
from random import randint
from login.models import OtpData
from sms import send_sms
def login_user(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    mobile = '9669997799'
                    otp = randint(100000,999999)
                    message = 'OTP for the App is '+str(otp)
                    send_sms(mobile,message)
                    otp_obj = OtpData()
                    otp_obj.mobile = mobile
                    otp_obj.otp = otp
                    otp_obj.save()
                    return render(request,'login/Otp_verify.html')

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


def verify(request):
    print('inside verify function')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        otp = request.POST['otp']
        mobile = request.POST['mobile']
        otp_list = OtpData.objects.all()
        for obj in otp_list:
            if obj.otp == int(otp) and obj.mobile == mobile:
                print('FOUND')
                login(request,user)
                print('User Verified')
                return redirect('http://127.0.0.1:8000/firm/firm_login')
        return render(request, 'login/Otp_verify.html')
    else:
        return render(request, 'login/Otp_verify.html')
