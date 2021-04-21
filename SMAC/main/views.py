from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from datetime import date, timedelta
from django.db import models
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from .forms import ImageForm
#all models Imports
from .models import Members
from .models import expence
from .models import Invoice
from .models import Balance
from .models import EmergencyFunds
from .models import FestivalFunds
from .models import SpecialPurposeFunds


#Global Variable

allm=Members.objects.filter(status='active').order_by('flat_no')
today=timezone.now()

# Create your views here.
def index(request):
    return render(request,'index.html')

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
 
def Home(request): 
    Bal=Balance.objects.get(id='1')
    month=today.strftime('%B')
    prev = date.today().replace(day=1) - timedelta(days=1)
    prevmon2 = date.today().replace(day=1) - timedelta(days=45)
    prev2=prevmon2.strftime('%B')
    prevmonth = prev.strftime('%B')
    year=today.year
    mem1=Members.objects.filter(status='active',paid_upto=prevmonth.upper()).order_by('flat_no')
    mem2=Members.objects.filter(status='active',paid_upto=prev2.upper()).order_by('flat_no')
    memy=Members.objects.filter(status='active',paid_upto=year).order_by('-paid_upto')
    params={'mem':mem1, 'bal':Bal,'allm':allm, 'mem2':mem2, 'memy':memy,'prevmonth':prevmonth, 'prev2':prev2 } 
    if not request.user.is_authenticated:
        return redirect("/")        
    else:
        return render(request,'home.html',params)

def Member(request):
    mem=Members.objects.filter(status='active').order_by('flat_no')
    n = len(mem)
    params={'mem':mem,'len':n} 
    if not User.is_authenticated:
        return redirect("/")
    else:
        return render(request,'Member.html',params)

def Expences(request):
    if request.method=="POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid:
            form.save()
            obj=form.instance
            a=obj.bill_amount
            cur=Balance.objects.get(id=1)
            b=a+cur.expence
            c=cur.balance-a
            print(b)
            be=Balance.objects.filter(id='1').update(expence=b, balance=c)
            return redirect("/Expences")
    else:
        bal=Balance.objects.get(id='1')
        exp=expence.objects.all()
        n = len(exp)
        form = ImageForm()
        params={'form':form,'exp':exp,'len':n,'bal':bal}
        return render(request,'Expences.html',params)

def Collection(request):
    Bal=Balance.objects.get(id='1')
    inv=Invoice.objects.filter(status='active').order_by('date')
    n = len(inv)
    params={'inv':inv,'len':n,'bal':Bal}
    return render(request,'Collection.html',params)

def Pending(request):
    mem=Members.objects.filter(mode='monthly',status='active').order_by('paid_upto')
    yer = Members.objects.filter(mode='yearly',status='active').order_by('paid_upto')
    year=today.year
    date=today.strftime('%B')
    params={'mem':mem, 'date':date.upper(), 'year':year, 'yer':yer, 'allm':allm}
    return render(request,'Pending.html',params)

def Funds(request):
    emf=EmergencyFunds.objects.filter(status='active')
    fef=FestivalFunds.objects.filter(status='active')
    spf=SpecialPurposeFunds.objects.filter(status='active')
    balem=Balance.objects.get(id='2')
    balsp=Balance.objects.get(id='4')
    balfes=Balance.objects.get(id='3')
    params={'allm':allm, 'emf':emf, 'fef':fef, 'spf':spf,'balem':balem,'balsp':balsp,'balfes':balfes}
    return render(request,'Funds.html',params)

#tut 30 for cmd database
def addmember(request):
    if request.method=="POST":
        name=request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        flat_no= request.POST['flat_no']
        join_date= request.POST['join_date']
        newmem= Members(name=name, email= email, contact=contact, flat_no=flat_no, join_date=join_date,mode='monthly', paid_upto='Not Yet', date_at="2021-01-01",status='active',del_reason="not now")
        newmem.save()
        return redirect("Member")
    else:
        return redirect("Member")


    return render(request,'Member.html')

def addinvoice(request):
    if request.method=="POST":
        payee=request.POST['payee']
        flat_no=request.POST['flat_no']
        month=request.POST['month']
        paymenttype=request.POST['paymenttype']
        amount=request.POST['amount']
        mode=request.POST['mode']
        date=timezone.now()
        invoice= Invoice(payee_name=payee, date=date, payment_method=paymenttype, flat_no=flat_no, for_month=month, amount=amount,status='active')
        invoice.save()
        getbal=Balance.objects.get(id='1')
        a=int(amount)+getbal.collection
        b=int(amount)+getbal.balance
        print(a)
        bal=Balance.objects.filter(id='1').update(collection=a,balance=b)
        mem=Members.objects.filter(flat_no=flat_no,status='active').update(paid_upto=month, date_at=date, mode=mode)
        inv=Invoice.objects.get(flat_no=flat_no,for_month=month)
        params={'inv':inv, 'allm':allm}
        return render(request,"bill.html",params)
    else:
        id=request.GET.get('id')
        inv=Invoice.objects.get(id=id)
        params={'inv':inv}
        return render(request,'bill.html',params)
    
def edit(request):
    if request.method== "POST":
        id=request.POST['id']
        name=request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        flat_no= request.POST['flat_no']
        join_date= request.POST['join_date']
        mem=Members.objects.filter(id=id).update(name=name, email= email, contact=contact, flat_no=flat_no, join_date=join_date)
        return redirect('Member')
    else:
        id=request.GET.get('id')
        edi=Members.objects.get(id=id)
        mem=Members.objects.filter(status='active').order_by('flat_no')
        params={'edit':edi,'mem':mem}
        return render(request,"edit.html",params)

def delete(request):
    if request.method=='POST':
        id=request.POST['id']
        rea=request.POST['reason']
        mem=Members.objects.filter(id=id).update(status='deleted', del_reason=rea)
        return redirect('Member')
    else:
        id=request.GET.get('id')
        dele=Members.objects.get(id=id)
        mem=Members.objects.filter(status='active').order_by('flat_no')
        params={'dele':dele, 'mem':mem}
        return render(request,'delete.html',params)

def delinv(request):
    if request.method=="POST":
        id=request.POST['id']
        rea=request.POST['reason']
        inv=Invoice.objects.filter(id=id).update(status='deleted',del_reason=rea)
        ina=Invoice.objects.get(id=id)
        bal=Balance.objects.get(id='1')
        am=bal.balance-ina.amount
        ac=bal.collection-ina.amount
        print(ac,am)
        d=Balance.objects.filter(id='1').update(collection=ac,balance=am)
        print(d)
        return redirect('Collection')
    else:
        id=request.GET.get('id')
        dele=Invoice.objects.get(id=id)
        Bal=Balance.objects.get(id='1')
        inv=Invoice.objects.filter(status="active").order_by('date')
        n = len(inv)
        params={'inv':inv,'len':n,'bal':Bal,'dele':dele}
        return render(request,'delinv.html',params)

def specialfunds(request):
    if request.method == "POST" :
        payee=request.POST['payee']
        flat_no=request.POST['flat_no']
        paymenttype=request.POST['paymenttype']
        amount=request.POST['amount']
        spe=request.POST['special']
        date=timezone.now()
        special=SpecialPurposeFunds(special_purpose=spe,payee_name=payee,date=date.date(), payment_method=paymenttype,flat_no=flat_no,amount=amount,status='active',del_reason='not yet')
        special.save()
        bal=Balance.objects.get(id='4')
        a=int(amount)+bal.balance
        b=int(amount)+bal.collection
        print(a,b)
        balup=Balance.objects.filter(id='4').update(collection=b,balance=a)
        return redirect('Funds')



def festivefunds(request):
    if request.method == "POST" :
        payee=request.POST['payee']
        flat_no=request.POST['flat_no']
        paymenttype=request.POST['paymenttype']
        amount=request.POST['amount']
        fes=request.POST['festive']
        date=timezone.now()
        festive=FestivalFunds(fistival_name=fes,payee_name=payee,date=date.date(), payment_method=paymenttype,flat_no=flat_no,amount=amount,status='active',del_reason='not yet')
        festive.save()
        bal=Balance.objects.get(id='3')
        a=int(amount)+bal.balance
        b=int(amount)+bal.collection
        print(a,b)
        balup=Balance.objects.filter(id='3').update(collection=b,balance=a)
        return redirect('Funds')


def emergencefunds(request):
    if request.method == "POST" :
        payee=request.POST['payee']
        flat_no=request.POST['flat_no']
        paymenttype=request.POST['paymenttype']
        amount=request.POST['amount']
        emer=request.POST['emergency']
        date=timezone.now()
        emergence=EmergencyFunds(Emergency_purpose=emer,payee_name=payee,date=date.date(), payment_method=paymenttype,flat_no=flat_no,amount=amount,status='active',del_reason='not yet')
        emergence.save()
        bal=Balance.objects.get(id='2')
        a=int(amount)+bal.balance
        b=int(amount)+bal.collection
        print(a,b)
        balup=Balance.objects.filter(id='2').update(collection=b,balance=a)
        return redirect('Funds')

def deleted(request):
    inv=Invoice.objects.filter(status='deleted')
    mem=Members.objects.filter(status='deleted')
    params={'inv':inv,'mem':mem}
    return render(request,'delobj.html',params)


dbdict={'1':'Current Account', 
'2':'emergency funds',
'3':'Festival Funds',
'4': 'Special purpose Funds'}