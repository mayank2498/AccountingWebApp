from django.shortcuts import render,redirect
from firm.models import Firm
from .models import Ledger
from .forms import LedgerForm
from django.core import serializers
from django.http import HttpResponse
from transaction.models import Transaction

def ledger_info(request,firm_id,ledger_id):
    ledger = Ledger.objects.filter(firm_id=int(firm_id),id=int(ledger_id))[0]
    print(ledger.name)
    return render(request,'home/ledger_info.html',{'id':firm_id,'ledger':ledger})

def ledger_home(request,firm_id):
    if request.user.is_authenticated():
        ledgers = Ledger.objects.filter(firm_id=int(firm_id))
        firm = Firm.objects.all()
        for obj in firm:
            if str(obj.id) == firm_id :
                name = obj.name
                year = obj.year
                break

        query = request.GET.get("q")
        if query is not None:
            ledgers = ledgers.filter(name__contains=query).distinct()
            for ledger in ledgers:
                amount = 0.0
                transactions = Transaction.objects.filter(ledger_id=ledger.id,ledger__firm_id=int(firm_id))
                for transaction in transactions:
                    if transaction.type == 'Credit':
                        amount += transaction.amount
                    else:
                        amount -= transaction.amount
                if amount < 0.0 :
                    ledger.amount = float(0-amount)
                    ledger.dominant = 'Debit'
                    ledger.save()
                else:
                    ledger.amount = amount
                    ledger.dominant = 'Credit'
                    ledger.save()
            return render(request,'home/ledger_home.html',{'ledgers':ledgers,'name':name,'year':year,'id':firm_id,'all':'active'})
        else:
            for ledger in ledgers:
                amount = 0.0
                transactions = Transaction.objects.filter(ledger_id=ledger.id,ledger__firm_id=int(firm_id))
                for transaction in transactions:
                    if transaction.type == 'Credit':
                        amount += transaction.amount
                    else:
                        amount -= transaction.amount
                if amount < 0.0 :
                    ledger.amount = float(0-amount)
                    ledger.dominant = 'Debit'
                    ledger.save()
                else:
                    ledger.amount = amount
                    ledger.dominant = 'Credit'
                    ledger.save()
            return render(request, 'home/ledger_home.html',
                          {'ledgers': ledgers, 'name': name, 'year': year, 'id': firm_id,'all':'active'})
    else:
        return render(request, 'login/login_admin.html')

def add_ledger(request,firm_id):
    if request.user.is_authenticated():
        form = LedgerForm(request.POST or None)
        if form.is_valid():
            ledger = form.save(commit=False)
            ledger.firm_id = int(firm_id)
            if(ledger.mobile_no == ""):
                ledger.mobile_no = "XXXXXXXXXX"
            if (ledger.pan_no == ""):
                ledger.pan_no = "XXXXXX"
            if (ledger.address == ""):
                ledger.address = "Not Specified"
            ledger.save()
            ledgers = Ledger.objects.filter(firm_id=int(firm_id))
            url = "/home/"+str(firm_id)+"/ledger_home"
            return redirect(url)
        else:
            return render(request,'home/add_ledger.html',{'form':form,'id':firm_id})
    else:
        return render(request,'login/login_admin.html')


def delete_ledger(request,firm_id,ledger_id):
    if request.user.is_authenticated():
        firm = Firm.objects.get(id=int(firm_id))
        ledger = Ledger.objects.filter(pk=int(ledger_id))
        ledger.delete()
        ledgers = Ledger.objects.filter(firm_id=int(firm_id))
        return render(request,'home/ledger_home.html',{'ledgers':ledgers,'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return render(request,'login/login_admin.html')

def update_ledger(request,firm_id,ledger_id):
    ledger_id = int(ledger_id)
    firm = Firm.objects.get(id=int(firm_id))
    if request.user.is_authenticated():
        if request.method == 'GET':
            ledger = Ledger.objects.filter(pk=ledger_id)[0]
            form = LedgerForm(instance=ledger)
            return render(request,'home/update_ledger.html', {'form': form,'name':firm.name,'year':firm.year,'id':firm.id})
        else:
            ledger = Ledger.objects.filter(pk=ledger_id)[0]
            form = LedgerForm(request.POST or None)
            if form.is_valid():
                print('VALID')
                ledger_form = form.save(commit=False)
                ledger.name = ledger_form.name
                ledger.address = ledger_form.address
                ledger.pan_no = ledger_form.pan_no
                ledger.mobile_no = ledger_form.mobile_no
                ledger.type = ledger_form.type
                ledger.save()
                ledgers = Ledger.objects.filter(firm_id=int(firm_id))
                return render(request,'home/ledger_home.html',{'ledgers':ledgers,'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return render(request, 'login/login_admin.html')


def ledger_json(request,firm_id):
    firm_id = int(firm_id)
    ledgers = Ledger.objects.filter(firm_id=firm_id)
    queryset = serializers.serialize('json', ledgers)
    return HttpResponse(queryset, content_type='application/json')


def filtersuppliers(request,firm_id):
    if request.user.is_authenticated():
        ledgers = Ledger.objects.filter(firm_id=int(firm_id),type='Supplier')
        firm = Firm.objects.all()
        for obj in firm:
            if str(obj.id) == firm_id :
                name = obj.name
                year = obj.year
                break
        return render(request, 'home/ledger_home.html',
                          {'ledgers': ledgers, 'name': name, 'year': year, 'id': firm_id,'supplier':'active'})
    else:
        return render(request, 'login/login_admin.html')



def filtercustomer(request,firm_id):
    if request.user.is_authenticated():
        ledgers = Ledger.objects.filter(firm_id=int(firm_id),type='Customer')
        firm = Firm.objects.all()
        for obj in firm:
            if str(obj.id) == firm_id :
                name = obj.name
                year = obj.year
                break
        return render(request, 'home/ledger_home.html',
                          {'ledgers': ledgers, 'name': name, 'year': year, 'id': firm_id,'customer':'active'})
    else:
        return render(request, 'login/login_admin.html')


def filteremployee(request,firm_id):
    if request.user.is_authenticated():
        ledgers = Ledger.objects.filter(firm_id=int(firm_id),type='Employee')
        firm = Firm.objects.all()
        for obj in firm:
            if str(obj.id) == firm_id :
                name = obj.name
                year = obj.year
                break
        return render(request, 'home/ledger_home.html',
                          {'ledgers': ledgers, 'name': name, 'year': year, 'id': firm_id,'employee':'active'})
    else:
        return render(request, 'login/login_admin.html')















