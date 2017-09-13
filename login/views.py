from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.conf.urls import url
from django.contrib.auth import authenticate,login,logout
from random import randint
from login.models import OtpData
from sms import send_sms
def login_user(request):
    if not request.user.is_authenticated():
        if 'user_id' in request.session:
            del request.session['user_id']
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            mobile = request.POST['mobile']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    otp = randint(100000,999999)
                    message = 'OTP for the App is '+str(otp)
                    send_sms(mobile,message)
                    otp_obj = OtpData()
                    otp_obj.mobile = mobile
                    otp_obj.otp = otp
                    otp_obj.flag = False
                    otp_obj.save()
                    #login(request,user)
                    request.session['user_id'] = user.id
                    request.session['otp_id'] = otp_obj.id
                    return render(request,'login/Otp_verify.html')
                else:
                    return render(request,'login/login_admin.html',{'error_message':'Your account has been disabled'})
            else:
                return render(request,'login/login_admin.html',{'error_message':'Invalid Username or Password. Login Again'})
        else:
            return render(request,'login/login_admin.html')
    else:
        return redirect('/firm/firm_login')

def logout_user(request):
    logout(request)
    return redirect('/login/')


def verify(request):
    if request.method == 'POST':
        print(request.session['user_id'])
        user = User.objects.filter(id=request.session['user_id'])[0]
        otp_obj = OtpData.objects.filter(id=request.session['otp_id'])[0]
        otp = request.POST['otp']
        otp_list = OtpData.objects.filter(mobile=otp_obj.mobile)
        for obj in otp_list:
            if obj.otp == int(otp):
                obj.flag = True
                obj.save()
                login(request,user)
                print('User Verified')
                return redirect('http://127.0.0.1:8000/firm/firm_login')
        return render(request, 'login/Otp_verify.html',{'message':'Invalid Otp. Try Again.'})
    else:
        return render(request, 'login/Otp_verify.html')
