from django.shortcuts import render,redirect
from firm.models import Firm
from home.models import Ledger,Voucher
from transaction.models import Transaction

def impress_home(request,firm_id):
    print(request.get_host())
    firm = Firm.objects.get(id=int(firm_id))
    impresses = Transaction.objects.filter(ledger__firm_id=int(firm_id),voucher_type='Impress')
    return render(request,'transaction/impress_home.html',{'impresses':impresses,'name':firm.name,'year':firm.year,'id':firm.id,'all':'active'})

def add_impress(request,firm_id):
    #delete_all()
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    if 'name' in request.session:
        ledger_name = request.session['name']
        del request.session['name']
        return render(request, 'transaction/add_impress.html',
                      {'name': firm.name, 'year': firm.year, 'id': firm.id, 'ledger_name': ledger_name})

    if request.user.is_authenticated():
        if request.method == 'POST':
            ledger = Ledger.objects.filter(firm_id=int(firm_id), name=request.POST['ledger'])[0]
            input_impress = Transaction()
            input_impress.ledger_id = ledger.id
            input_impress.amount = request.POST['amount']
            input_impress.mode = request.POST['mode']
            v_no = request.POST['voucher_no']
            ledgers = Ledger.objects.filter(firm_id=firm_id)
            data = check_voucher_no(v_no, firm_id)
            if data[0]:
                obj = Transaction.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                return render(request, 'transaction/add_impress.html',
                              {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                'failure': 'True', 'obj': obj,
                               'input_impress':input_impress,'v_no':v_no
                               })
            for ledger in ledgers:
                if ledger.name == request.POST['ledger']:
                    voucher_new = Voucher()
                    voucher_new.voucher_no = request.POST['voucher_no']
                    voucher_new.save()
                    impress = Transaction()
                    impress.ledger_id = ledger.pk
                    impress.amount = request.POST['amount']
                    impress.mode = request.POST['mode']
                    impress.description = request.POST['description']
                    impress.voucher_id = voucher_new.pk
                    impress.type = 'Credit'
                    impress.voucher_type = 'Impress'
                    impress.save()
                    cash = Transaction()
                    CASH = Ledger.objects.filter(firm_id=int(firm_id), name='Cash')[0]
                    cash.ledger_id = CASH.id
                    cash.voucher_type = 'Journal'
                    cash.description = impress.description
                    cash.amount = impress.amount
                    cash.mode = impress.mode
                    cash.type = 'Debit'
                    cash.save()
                    message = "Imprest Data has been saved !"
                    impresses = Transaction.objects.filter(ledger__firm_id=int(firm_id),voucher_type='Impress')
                    return render(request, 'transaction/impress_home.html', {'impresses':impresses,'message': message,'name':firm.name,'year':firm.year,'id':firm.id})

            return render(request, 'transaction/impress_home.html',{'name':firm.name,'year':firm.year,'id':firm.id})
        else:
            return render(request,'transaction/add_impress.html',{'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return redirect('/login')


def expense_home(request,firm_id):
    firm = Firm.objects.get(id=int(firm_id))
    expenses = Transaction.objects.filter(ledger__firm_id=int(firm_id),voucher_type='Expense')
    return render(request,'transaction/expense_home.html',{'expenses':expenses,'name':firm.name,'year':firm.year,'id':firm.id,'all':'active'})



def add_expense(request,firm_id):
    #delete_all()
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    if 'name' in request.session:
        ledger_name = request.session['name']
        del request.session['name']
        return render(request, 'transaction/add_expense.html',
                      {'name': firm.name, 'year': firm.year, 'id': firm.id, 'ledger_name': ledger_name})
    if request.user.is_authenticated():
        if request.method == 'POST':
            ledger = Ledger.objects.filter(firm_id=int(firm_id), name=request.POST['ledger'])[0]
            input_expense = Transaction()
            input_expense.ledger_id = ledger.id
            input_expense.amount = request.POST['amount']
            input_expense.mode = request.POST['mode']
            ledgers = Ledger.objects.filter(firm_id=firm_id)
            v_no = request.POST['voucher_no']
            data = check_voucher_no(v_no, firm_id)
            if data[0]:
                obj = Transaction.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                return render(request, 'transaction/add_expense.html',
                              {'name': firm.name, 'year': firm.year, 'id': firm.id,
                                'failure': 'True', 'obj': obj,
                               'input_expense':input_expense,'v_no':v_no
                               })
            for ledger in ledgers:
                if ledger.name == request.POST['ledger']:
                    voucher_new = Voucher()
                    voucher_new.voucher_no = request.POST['voucher_no']
                    voucher_new.save()
                    expense = Transaction()
                    expense.ledger_id = ledger.pk
                    expense.amount = request.POST['amount']
                    expense.mode = request.POST['mode']
                    expense.description = request.POST['description']
                    expense.voucher_id = voucher_new.pk
                    expense.type = 'Credit'
                    expense.voucher_type = 'Expense'
                    expense.save()
                    cash = Transaction()
                    CASH = Ledger.objects.filter(firm_id=int(firm_id), name='Cash')[0]
                    cash.ledger_id = CASH.id
                    cash.voucher_type = 'Journal'
                    cash.description = expense.description
                    cash.amount = expense.amount
                    cash.mode = expense.mode
                    cash.type = 'Debit'
                    cash.save()
                    message = "Expense Data has been saved !"
                    expenses = Transaction.objects.filter(ledger__firm_id=int(firm_id),voucher_type='Expense')
                    return render(request, 'transaction/expense_home.html', {'expenses':expenses,'message': message,'name':firm.name,'year':firm.year,'id':firm.id})

            return render(request, 'transaction/expense_home.html',{'name':firm.name,'year':firm.year,'id':firm.id})
        else:
            return render(request,'transaction/add_expense.html',{'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return redirect('/login')


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
    receives = Transaction.objects.filter(ledger__firm_id=int(firm_id),voucher_type='Receive')
    return render(request,'transaction/receive_home.html',{'receives':receives,'name':firm.name,'year':firm.year,'id':firm.id,'all':'active'})


def add_receive(request,firm_id):
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    if 'name' in request.session:
        ledger_name = request.session['name']
        del request.session['name']
        return render(request, 'transaction/add_receive.html',
                      {'name': firm.name, 'year': firm.year, 'id': firm.id, 'ledger_name': ledger_name})
    if request.user.is_authenticated():
        if request.method == 'POST':
            ledger = Ledger.objects.filter(firm_id=int(firm_id), name=request.POST['ledger'])[0]
            input_receive = Transaction()
            input_receive.ledger_id = ledger.id
            input_receive.amount = request.POST['amount']
            input_receive.mode = request.POST['mode']
            ledgers = Ledger.objects.filter(firm_id=firm_id)
            v_no = request.POST['voucher_no']
            data = check_voucher_no(v_no, firm_id)
            if data[0]:
                obj = Transaction.objects.filter(voucher__voucher_no=v_no,ledger__firm_id=firm_id)[0]
                return render(request, 'transaction/add_receive.html',
                              {'name': firm.name, 'year': firm.year, 'id': firm.id,
                               'category': 'Impress', 'failure': 'True', 'obj': obj,
                               'input_receive':input_receive,'v_no':v_no
                               })
            for ledger in ledgers:
                if ledger.name == request.POST['ledger']:
                    voucher_new = Voucher()
                    voucher_new.voucher_no = request.POST['voucher_no']
                    voucher_new.save()
                    receive = Transaction()
                    receive.ledger_id = ledger.pk
                    receive.amount = request.POST['amount']
                    receive.mode = request.POST['mode']
                    receive.description = request.POST['description']
                    receive.voucher_id = voucher_new.pk
                    receive.type = 'Debit'
                    receive.voucher_type = 'Receive'
                    receive.save()
                    cash = Transaction()
                    CASH = Ledger.objects.filter(firm_id=int(firm_id), name='Cash')[0]
                    cash.ledger_id = CASH.id
                    cash.voucher_type = 'Journal'
                    cash.description = receive.description
                    cash.amount = receive.amount
                    cash.mode = receive.mode
                    cash.type = 'Credit'
                    cash.save()
                    message = "Receive Data has been saved !"
                    receives = Transaction.objects.filter(ledger__firm_id=int(firm_id),voucher_type='Receive')
                    return render(request, 'transaction/receive_home.html', {'receives':receives,'message': message,'name':firm.name,'year':firm.year,'id':firm.id})

            return render(request, 'transaction/receive_home.html',{'name':firm.name,'year':firm.year,'id':firm.id})
        else:
            return render(request,'transaction/add_receive.html',{'name':firm.name,'year':firm.year,'id':firm.id})
    else:
        return redirect('/login')

def check_voucher_no(v_no,firm_id):
    transactions = Transaction.objects.filter(ledger__firm_id=int(firm_id))
    for obj in transactions:
        if obj.voucher_id != -1 and obj.voucher.voucher_no == v_no :
            return [True,obj.voucher_type]
    return [False,'success']

def ledger_details(request,firm_id,ledger_id):
    if request.method == "POST":
        name = request.POST['name']
        amount = request.POST['amount']
        type = request.POST['type']
        v_no = request.POST['voucher']
        description = request.POST['description']
        try :
            x = Ledger.objects.filter(name=name,firm_id=int(firm_id))[0]
            y = Transaction.objects.filter(voucher__voucher_no=v_no,ledger__name=name)[0]
        except Exception as e:
            amount = 0.0
            type = 'Credit'
            firm = Firm.objects.get(id=int(firm_id))
            firm_id = int(firm_id)
            ledger = Ledger.objects.get(id=int(ledger_id))
            transactions = Transaction.objects.filter(ledger__firm_id=firm_id, ledger__name=ledger.name)
            for transaction in transactions:
                if transaction.type == 'Credit':
                    amount += transaction.amount
                else:
                    amount -= transaction.amount
            if amount < 0.0:
                amount = float(0 - amount)
                type = 'Debit'

            return render(request, 'transaction/ledger_details.html', {'transactions': transactions,
                                                                       'name': firm.name, 'year': firm.year,
                                                                       'id': firm.id, 'ledger': ledger,
                                                                       'amount': amount, 'type': type,
                                                                       'error':'Invalid Details'
                                                                       })

    else:
        amount = 0.0
        type = 'Credit'
        firm = Firm.objects.get(id=int(firm_id))
        firm_id = int(firm_id)
        ledger = Ledger.objects.get(id=int(ledger_id))
        transactions = Transaction.objects.filter(ledger__firm_id=firm_id,ledger__name=ledger.name)
        for transaction in transactions:
            if transaction.type == 'Credit':
                amount += transaction.amount
            else:
                amount -= transaction.amount
        if amount < 0.0 :
            amount = float(0-amount)
            type = 'Debit'

        return render(request,'transaction/ledger_details.html',{'transactions':transactions,
                                                                 'name':firm.name,'year':firm.year,'id':firm.id,'ledger':ledger, 'amount':amount,'type':type
                                                                 })


def filter_suppliers(request,firm_id,type_id):
    firm = Firm.objects.get(id=int(firm_id))
    if type_id == '1':
        expenses = Transaction.objects.filter(ledger__firm_id=int(firm_id),ledger__type='Supplier')
        return render(request, 'transaction/expense_home.html',
                      {'expenses': expenses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'supplier':'active'})
    elif type_id == '2':
        impresses = Transaction.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Supplier')
        return render(request, 'transaction/impress_home.html',
                      {'impresses': impresses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'supplier':'active'})
    else :
        receives = Transaction.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Supplier')
        return render(request, 'transaction/receive_home.html',
                      {'receives': receives , 'name': firm.name, 'year': firm.year, 'id': firm.id,'supplier':'active'})

def filter_customers(request,firm_id,type_id):
    firm = Firm.objects.get(id=int(firm_id))
    if type_id == '1':
        expenses = Transaction.objects.filter(ledger__firm_id=int(firm_id),ledger__type='Customer')
        return render(request, 'transaction/expense_home.html',
                      {'expenses': expenses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'customer':'active'})
    elif type_id == '2':
        impresses = Transaction.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Customer')
        return render(request, 'transaction/impress_home.html',
                      {'impresses': impresses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'customer':'active'})
    else :
        receives = Transaction.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Customer')
        return render(request, 'transaction/receive_home.html',
                      {'receives': receives , 'name': firm.name, 'year': firm.year, 'id': firm.id,'customer':'active'})

def filter_employees(request,firm_id,type_id):
    firm = Firm.objects.get(id=int(firm_id))
    if type_id == '1':
        expenses = Transaction.objects.filter(ledger__firm_id=int(firm_id),ledger__type='Employee')
        return render(request, 'transaction/expense_home.html',
                      {'expenses': expenses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'employee':'active'})
    elif type_id == '2':
        impresses = Transaction.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Employee')
        return render(request, 'transaction/impress_home.html',
                      {'impresses': impresses, 'name': firm.name, 'year': firm.year, 'id': firm.id,'employee':'active'})
    else :
        receives = Transaction.objects.filter(ledger__firm_id=int(firm_id), ledger__type='Employee')
        return render(request, 'transaction/receive_home.html',
                      {'receives': receives , 'name': firm.name, 'year': firm.year, 'id': firm.id,'employee':'active'})


def add_transaction(request,firm_id,type_id,ledger_id):
    print(type_id)
    if type_id == '1':
        ledger = Ledger.objects.filter(id=ledger_id)[0]
        request.session['name'] = ledger.name
        url = '/transaction/'+str(firm_id)+'/add_impress'
        return redirect(url)
    if type_id == '2':
        ledger = Ledger.objects.filter(id=ledger_id)[0]
        request.session['name'] = ledger.name
        url = '/transaction/' + str(firm_id) + '/add_expense'
        return redirect(url)
    if type_id == '3':
        ledger = Ledger.objects.filter(id=ledger_id)[0]
        request.session['name'] = ledger.name
        url = '/transaction/' + str(firm_id) + '/add_receive'
        return redirect(url)

def add_journal(request,firm_id):
    if request.method == 'POST':
        ledger_main = request.POST['ledger_main']
        try:
            ledger = Ledger.objects.filter(firm_id=int(firm_id),name=ledger_main)[0]
        except Exception as e:
            print(e)
            return render(request, 'transaction/add_journal.html',
                          {'id': int(firm_id), 'message': 'Main Ledger does not exist'})

        description_main = request.POST['description_main']
        type_main  = request.POST['type_main']

        names = request.POST.getlist('name')
        vouchers = request.POST.getlist('voucher')
        del vouchers[len(names)-1]
        amounts = request.POST.getlist('amount')
        descriptions = request.POST.getlist('description')
        transactions = Transaction.objects.filter(ledger__firm__id=int(firm_id),voucher__voucher_no__in=vouchers)
        if len(transactions) > 0 :
            return render(request, 'transaction/add_journal.html',
                          {'id': int(firm_id), 'message': 'A Voucher Number already exists'})

        for i in range(len(names)-1):  #check if all ledgers are valid
            try:
                ledger = Ledger.objects.filter(firm_id=int(firm_id),name=names[i])[0]
            except Exception as e:
                print(e)
                return render(request,'transaction/add_journal.html', {'id': int(firm_id),'message':'Ledger does not exist'})

        print('ready to save journal entry')
        amount = 0.0
        type = 'Credit'
        if type_main != 'Debit' :
            type = 'Debit'
        for i in range(len(vouchers)):
            amount += float(amounts[i])
            ledger = Ledger.objects.filter(firm_id=int(firm_id),name=names[i])[0]
            transaction = Transaction()
            transaction.ledger_id = ledger.id
            transaction.type = type
            transaction.description = descriptions[i]
            voucher = Voucher()
            voucher.voucher_no = vouchers[i]
            voucher.save()
            transaction.voucher_id = voucher.id
            transaction.amount = amounts[i]
            transaction.save()
        ledger = Ledger.objects.filter(firm_id=int(firm_id), name=ledger_main)[0]
        transaction = Transaction()
        transaction.ledger_id = ledger.id
        transaction.type = type_main
        transaction.description = description_main
        voucher = Voucher()
        voucher.voucher_no = -1
        voucher.save()
        transaction.voucher_id = voucher.id
        transaction.amount = amount
        transaction.save()
        return render(request, 'transaction/add_journal.html', {'id': int(firm_id), 'message': 'Success. Transactions have been saved'})
    else:
        if request.user.is_authenticated():
            return render(request,'transaction/add_journal.html',{'id':int(firm_id)})
        else:
            return redirect('/login')
def delete_all():
    Transaction.objects.all().delete()

def transaction_add(request,firm_id,ledger_id):
    amount = request.POST['amount']
    v_no = request.POST['voucher']
    description = request.POST['description']
    type = request.POST['type']
    try:
        voucher = Transaction.objects.filter(ledger__firm__id=int(firm_id),voucher__voucher_no=int(v_no))
    except Exception as e:
        amount = 0.0
        type = 'Credit'
        firm = Firm.objects.get(id=int(firm_id))
        firm_id = int(firm_id)
        ledger = Ledger.objects.get(id=int(ledger_id))
        transactions = Transaction.objects.filter(ledger__firm_id=firm_id, ledger__name=ledger.name)
        transactions = sorted(transactions, key=lambda x: x.created,reverse=True)
        for transaction in transactions:
            if transaction.type == 'Credit':
                amount += transaction.amount
            else:
                amount -= transaction.amount
        if amount < 0.0:
            amount = float(0 - amount)
            type = 'Debit'

        return render(request, 'transaction/ledger_details.html', {'transactions': transactions,
                                                                   'name': firm.name, 'year': firm.year,'id':firm.id,
                                                                   'error':'Voucher number already exists',
                                                                   'ledger': ledger, 'amount': amount, 'type': type
                                                                   })
    ledger = Ledger.objects.get(id=int(ledger_id))
    transaction = Transaction()
    transaction.ledger_id = ledger.id
    voucher = Voucher()
    voucher.voucher_no = str(v_no)
    voucher.save()
    transaction.voucher_id = voucher.id
    transaction.amount = float(amount)
    transaction.voucher_type = type
    transaction.description = description
    if type=='Impress' or type == 'Expense':
        transaction.type = 'Credit'
        cash_ledger = Ledger.objects.filter(name="Cash",firm_id=int(firm_id))[0]
        cash = Transaction()
        voucher = Voucher()
        voucher.voucher_no = -1
        voucher.save()
        cash.voucher_id = voucher.id
        cash.ledger_id = cash_ledger.id
        cash.amount = float(amount)
        cash.type = 'Debit'
        cash.save()
    elif type == 'Receive':
        transaction.type = 'Debit'
        cash_ledger = Ledger.objects.filter(name="Cash", firm_id=int(firm_id))[0]
        cash = Transaction()
        voucher = Voucher()
        voucher.voucher_no = -1
        voucher.save()
        cash.voucher_id = voucher.id
        cash.ledger_id = cash_ledger.id
        cash.amount = float(amount)
        cash.type = 'Credit'
        cash.save()
    transaction.save()
    amount = 0.0
    type = 'Credit'
    firm = Firm.objects.get(id=int(firm_id))
    firm_id = int(firm_id)
    ledger = Ledger.objects.get(id=int(ledger_id))
    transactions = Transaction.objects.filter(ledger__firm__id=firm_id, ledger__name=ledger.name)
    transactions = sorted(transactions, key=lambda x: x.created,reverse=True)
    for transaction in transactions:
        if transaction.type == 'Credit':
            amount += transaction.amount
        else:
            amount -= transaction.amount
    if amount < 0.0:
        amount = float(0 - amount)
        type = 'Debit'

    return render(request, 'transaction/ledger_details.html', {'transactions': transactions,
                                                               'name': firm.name, 'year': firm.year, 'id': firm.id,
                                                               'ledger': ledger, 'amount': amount, 'type': type
                                                               })





















