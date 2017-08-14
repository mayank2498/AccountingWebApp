from django.shortcuts import render,redirect
from firm.models import Firm
from home.models import Ledger,Voucher
from transaction.models import Impress,Expense,Receive

def impress_home(request,firm_id):
    firm = Firm.objects.get(id=int(firm_id))
    impresses = Impress.objects.filter(ledger__firm_id=int(firm_id))
    return render(request,'transaction/impress_home.html',{'impresses':impresses,'name':firm.name,'year':firm.year,'id':firm.id,'all':'active'})

def add_impress(request,firm_id):
    #delete_all()
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    if request.user.is_authenticated():
        if request.method == 'POST':
            ledger = Ledger.objects.filter(firm_id=int(firm_id), name=request.POST['ledger'])[0]
            input_impress = Impress()
            input_impress.ledger_id = ledger.id
            input_impress.amount = request.POST['amount']
            input_impress.transaction_type = request.POST['transaction_type']
            ledgers = Ledger.objects.filter(firm_id=firm_id)
            v_no = request.POST['voucher_no']
            ledgers = Ledger.objects.filter(firm_id=firm_id)
            data = check_voucher_no(v_no, firm_id)
            if data[0]:
                type = data[1]
                if type == 'impress':
                    impress = Impress.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_impress.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Impress', 'failure': 'True', 'obj': impress,
                                   'input_impress':input_impress,'v_no':v_no
                                   })
                elif type == 'expense':
                    expense = Expense.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_impress.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Expense', 'failure': 'True', 'obj': expense,
                                   'input_impress': input_impress, 'v_no': v_no
                                   })
                else:
                    receive = Receive.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_impress.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Receive', 'failure': 'True', 'obj': receive,
                                   'input_impress': input_impress, 'v_no': v_no
                                   })
            for ledger in ledgers:
                if ledger.name == request.POST['ledger']:
                    voucher_new = Voucher()
                    voucher_new.voucher_no = request.POST['voucher_no']
                    voucher_new.save()
                    impress = Impress()
                    impress.ledger_id = ledger.pk
                    impress.amount = request.POST['amount']
                    impress.transaction_type = request.POST['transaction_type']
                    impress.description = request.POST['description']
                    impress.amount_left = impress.amount
                    impress.voucher_id = voucher_new.pk
                    impress.save()
                    message = "Impress Data has been saved !"
                    impresses = Impress.objects.filter(ledger__firm_id=int(firm_id))
                    return render(request, 'transaction/impress_home.html', {'impresses':impresses,'message': message,'name':firm.name,'year':firm.year,'id':firm.id})

            return render(request, 'transaction/impress_home.html',{'name':firm.name,'year':firm.year,'id':firm.id})
        else:
            return render(request,'transaction/add_impress.html',{'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return redirect('http://127.0.0.1:8000/login')


def expense_home(request,firm_id):
    firm = Firm.objects.get(id=int(firm_id))
    expenses = Expense.objects.filter(ledger__firm_id=int(firm_id))
    return render(request,'transaction/expense_home.html',{'expenses':expenses,'name':firm.name,'year':firm.year,'id':firm.id,'all':'active'})



def add_expense(request,firm_id):
    #delete_all()
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    if request.user.is_authenticated():
        if request.method == 'POST':
            ledger = Ledger.objects.filter(firm_id=int(firm_id), name=request.POST['ledger'])[0]
            print(ledger.name+ledger.type)
            input_expense = Expense()
            input_expense.ledger_id = ledger.id
            input_expense.amount = request.POST['amount']
            input_expense.transaction_type = request.POST['transaction_type']
            ledgers = Ledger.objects.filter(firm_id=firm_id)
            v_no = request.POST['voucher_no']
            data = check_voucher_no(v_no, firm_id)
            if data[0]:
                type = data[1]
                if type == 'impress':
                    impress = Impress.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_expense.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category':'Impress','failure':'True','obj':impress,
                                   'input_expense':input_expense,'v_no':v_no
                                   })
                elif type == 'expense':
                    expense = Expense.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_expense.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Expense', 'failure': 'True','obj':expense,
                                   'input_expense': input_expense,'v_no':v_no
                                   })
                else:
                    receive = Receive.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_expense.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Receive', 'failure': 'True', 'obj':receive,
                                   'input_expense': input_expense,'v_no':v_no
                                   })
            for ledger in ledgers:
                if ledger.name == request.POST['ledger']:
                    voucher_new = Voucher()
                    voucher_new.voucher_no = request.POST['voucher_no']
                    voucher_new.save()
                    expense = Expense()
                    expense.ledger_id = ledger.pk
                    expense.amount = request.POST['amount']
                    expense.voucher_id = voucher_new.pk
                    expense.transaction_type = request.POST['transaction_type']
                    expense.amount_left = expense.amount
                    expense.description = request.POST['description']
                    expense.save()
                    update_impress(expense,firm_id,float(expense.amount))
                    message = "Impress Data has been saved !"
                    expenses = Expense.objects.filter(ledger__firm_id=int(firm_id))
                    return render(request, 'transaction/expense_home.html', {'expenses':expenses,'message': message,'name':firm.name,'year':firm.year,'id':firm.id})

            return render(request, 'transaction/expense_home.html',{'name':firm.name,'year':firm.year,'id':firm.id})
        else:
            return render(request,'transaction/add_expense.html',{'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return redirect('http://127.0.0.1:8000/login')


def update_impress(expense,firm_id,expense_amount):
    impresses = Impress.objects.filter(ledger__firm_id=firm_id,ledger__name=expense.ledger.name)
    impresses = sorted(impresses, key=lambda x: x.created)
    for obj in impresses:
        if obj.amount_left != 0.0:
            if obj.amount_left > expense_amount :
                expense.amount_left = 0.0
                expense.save()
                obj.amount_left -= expense_amount
                obj.save()
                break
            else:
                expense.amount_left -= float(obj.amount_left)
                expense.save()
                expense_amount -= obj.amount_left
                obj.amount_left = 0.0
                obj.pending = False
                obj.save()
                update_impress(expense,firm_id,expense_amount)
                break




def receive_home(request,firm_id):
    firm = Firm.objects.get(id=int(firm_id))
    receives = Receive.objects.filter(ledger__firm_id=int(firm_id))
    return render(request,'transaction/receive_home.html',{'receives':receives,'name':firm.name,'year':firm.year,'id':firm.id,'all':'active'})


def add_receive(request,firm_id):
    #delete_all()
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    if request.user.is_authenticated():
        if request.method == 'POST':
            ledger = Ledger.objects.filter(firm_id=int(firm_id), name=request.POST['ledger'])[0]
            input_receive = Receive()
            input_receive.ledger_id = ledger.id
            input_receive.amount = request.POST['amount']
            input_receive.transaction_type = request.POST['transaction_type']
            ledgers = Ledger.objects.filter(firm_id=firm_id)
            v_no = request.POST['voucher_no']
            data = check_voucher_no(v_no, firm_id)
            if data[0]:
                type = data[1]
                if type == 'impress':
                    impress = Impress.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_expense.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Impress', 'failure': 'True', 'obj': impress,
                                   'input_receive':input_receive,'v_no':v_no
                                   })
                elif type == 'expense':
                    expense = Expense.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_receive.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Expense', 'failure': 'True', 'obj': expense,
                                   'input_receive': input_receive, 'v_no': v_no
                                   })
                else:
                    receive = Receive.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                    return render(request, 'transaction/add_receive.html',
                                  {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                   'category': 'Receive', 'failure': 'True', 'obj': receive,
                                   'input_receive': input_receive, 'v_no': v_no
                                   })
            for ledger in ledgers:
                if ledger.name == request.POST['ledger']:
                    voucher_new = Voucher()
                    voucher_new.voucher_no = request.POST['voucher_no']
                    voucher_new.save()
                    receive = Receive()
                    receive.ledger_id = ledger.pk
                    receive.amount = request.POST['amount']
                    receive.transaction_type = request.POST['transaction_type']
                    receive.description = request.POST['description']
                    receive.voucher_id = voucher_new.pk
                    receive.save()
                    message = "Impress Data has been saved !"
                    receives = Receive.objects.filter(ledger__firm_id=int(firm_id))
                    return render(request, 'transaction/receive_home.html', {'receives':receives,'message': message,'name':firm.name,'year':firm.year,'id':firm.id})

            return render(request, 'transaction/receive_home.html',{'name':firm.name,'year':firm.year,'id':firm.id})
        else:
            return render(request,'transaction/add_receive.html',{'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return redirect('http://127.0.0.1:8000/login')


def check_voucher_no(v_no,firm_id):
    impresses = Impress.objects.filter(ledger__firm_id=firm_id)
    expenses = Expense.objects.filter(ledger__firm_id=firm_id)
    receives = Receive.objects.filter(ledger__firm_id=firm_id)
    for obj in impresses:
        if obj.voucher.voucher_no == v_no :
            return [True,'impress']
    for obj in expenses:
        if obj.voucher.voucher_no == v_no :
            return [True,'expense']
    for obj in receives:
        if obj.voucher.voucher_no == v_no :
            return [True,'receive']
    return [False,'success']

def ledger_details(request,firm_id,ledger_id):
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    ledger = Ledger.objects.get(id=int(ledger_id))
    impresses = Impress.objects.filter(ledger__firm_id=firm_id,ledger__name=ledger.name)
    expenses = Expense.objects.filter(ledger__firm_id=firm_id,ledger__name=ledger.name)
    receives = Receive.objects.filter(ledger__firm_id=firm_id,ledger__name=ledger.name)
    return render(request,'transaction/ledger_details.html',{'impresses':impresses,
                                                             'expenses':expenses,
                                                             'receives':receives,'name':firm.name,'year':firm.year,'id':firm.id,'ledger':ledger
                                                             })


def filter_suppliers(request,firm_id,type_id):
    firm = Firm.objects.get(id=int(firm_id))
    if type_id == '1':
        expenses = Expense.objects.filter(ledger__firm_id=int(firm_id),ledger__type='Supplier')
        return render(request, 'transaction/expense_home.html',
                      {'expenses': expenses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'supplier':'active'})
    elif type_id == '2':
        impresses = Impress.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Supplier')
        return render(request, 'transaction/impress_home.html',
                      {'impresses': impresses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'supplier':'active'})
    else :
        receives = Receive.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Supplier')
        return render(request, 'transaction/receive_home.html',
                      {'receives': receives , 'name': firm.name, 'year': firm.year, 'id': firm.id,'supplier':'active'})

def filter_customers(request,firm_id,type_id):
    firm = Firm.objects.get(id=int(firm_id))
    if type_id == '1':
        expenses = Expense.objects.filter(ledger__firm_id=int(firm_id),ledger__type='Customer')
        return render(request, 'transaction/expense_home.html',
                      {'expenses': expenses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'customer':'active'})
    elif type_id == '2':
        impresses = Impress.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Customer')
        return render(request, 'transaction/impress_home.html',
                      {'impresses': impresses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'customer':'active'})
    else :
        receives = Receive.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Customer')
        return render(request, 'transaction/receive_home.html',
                      {'receives': receives , 'name': firm.name, 'year': firm.year, 'id': firm.id,'customer':'active'})

def filter_employees(request,firm_id,type_id):
    firm = Firm.objects.get(id=int(firm_id))
    if type_id == '1':
        expenses = Expense.objects.filter(ledger__firm_id=int(firm_id),ledger__type='Employee')
        return render(request, 'transaction/expense_home.html',
                      {'expenses': expenses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'employee':'active'})
    elif type_id == '2':
        impresses = Impress.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Employee')
        return render(request, 'transaction/impress_home.html',
                      {'impresses': impresses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'employee':'active'})
    else :
        receives = Receive.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Employee')
        return render(request, 'transaction/receive_home.html',
                      {'receives': receives , 'name': firm.name, 'year': firm.year, 'id': firm.id,'employee':'active'})


def pending_impresses(request,firm_id):
    firm = Firm.objects.get(id=int(firm_id))
    impresses = Impress.objects.filter(ledger__firm_id=int(firm_id),pending=True)
    return render(request, 'transaction/impress_home.html',
                  {'impresses': impresses, 'name': firm.name, 'year': firm.year, 'id': firm.id, 'all': 'active'})


























