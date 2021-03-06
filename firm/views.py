from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Firm
from .forms import FirmForm
from home.models import Ledger
from transaction.models import Transaction,Voucher

def add_firm(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            print('INside POSt')
            name = request.POST['firm_name']
            year = request.POST['firm_year']
            password = request.POST['pass']
            password_1 = request.POST['pass_1']
            if password == password_1 :
                firm = Firm()
                firm.name = name
                firm.year = year
                firm.password = password
                firm.save()
                print('Firm Data saved')
                ledger = Ledger()
                ledger.name = 'Cash'
                ledger.address = 'none'
                ledger.mobile_no = 'none'
                ledger.pan_no = 'none'
                ledger.type = 'Personal'
                ledger.firm_id = firm.id
                ledger.save()
                if request.POST['cash'] != "True" :
                    amount = request.POST['balance']
                    type = request.POST['type']
                    entry = Transaction()
                    entry.ledger_id = ledger.id
                    entry.description = "opening balance entered"
                    if type == 'D':
                        entry.type = 'Debit'
                    else :
                        entry.type = 'Credit'
                    voucher = Voucher()
                    voucher.voucher_no = -1
                    voucher.save()
                    entry.voucher_id = voucher.id
                    entry.voucher_type = 'Opening'
                    entry.amount = amount
                    entry.save()
                    return redirect('/firm/firm_login')
                else:
                    print('no opening balance')
                return redirect('/firm/firm_login')
            else:
                return render(request,'firm/add_firm.html',{'message':'Your passwords do not match !'})
        else:
            return render(request, 'firm/add_firm.html')
    else:
        return redirect('/login')


def firm_login(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            firm = Firm.objects.all()
            for obj in firm:
                if obj.name == request.POST['firm_name']:
                    if str(obj.password) == request.POST['password']:
                        url = '/home/'+str(obj.id)+'/ledger_home'
                        print('Logging in ')
                        return redirect(url)
                    else:
                        return render(request, 'firm/firm_login.html', {'message': 'Wrong Password!!'})
            else:
                return render(request,'firm/firm_login.html',{'message':'Sorry ! Could not find the firm '})
        else:
            return render(request, 'firm/firm_login.html')
    else:
        return redirect('/login')

def manage_firms(request):
    if request.user.is_authenticated():
        firms = Firm.objects.all()
        return render(request,'firm/firm_home.html',{'firms':firms})
    else:
        return redirect('/login')

def update_firm(request,firm_id):
    firm = Firm.objects.get(id=int(firm_id))
    if request.user.is_authenticated():
        if request.method == "GET":
            form = FirmForm(instance=firm)
            return render(request,'firm/update_firm.html',{'form': form})
        else:
            form = FirmForm(request.POST or None)
            if form.is_valid():
                firm_obj = form.save(commit=False)
                firm.name = firm_obj.name
                firm.year = firm_obj.year
                firm.save()
                return render(request,'firm/firm_home.html',{'firms':Firm.objects.all()})

    else:
        return render(request, 'login/login_admin.html')

def delete_firm(request,firm_id):
    if request.user.is_authenticated():
        firm = Firm.objects.get(id=int(firm_id))
        firm.delete()
        return redirect('/firm/manage_firms')
    else:
        return render(request, 'login/login_admin.html')


