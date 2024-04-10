from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here
@login_required(login_url='/admin_login/')
def index(request):
    client = client_detail.objects.all()
    counter=0
    for i in client:
        counter+=1
        
    case=case_detail.objects.all()
    case_counter=0
    for i in case:
        case_counter+=1

    team_members = team_member.objects.all()
    team_counter=0
    for i in team_members:
        team_counter+=1

    close = "close"
    status=case_detail.objects.filter(case_status_name=close)
    close_counter=0
    for i in status:
        close_counter+=1
       
    open = "open"
    status=case_detail.objects.filter(case_status_name=open)
    open_counter=0
    for i in status:
        open_counter+=1
    
    pending = "pending"
    status=case_detail.objects.filter(case_status_name=pending)
    pending_counter=0
    for i in status:
        pending_counter+=1

    dic ={'pending_counter':pending_counter,
          'open_counter':open_counter,'close_counter':close_counter,"pendings":status,
          'clients':counter,'cases':case,'case_counter':case_counter,
          'team_counter':team_counter,'team_members':team_members}
    return render(request,'index.html',context=dic)


# ............Client Detail Start..........
@login_required(login_url='/admin_login/')
def add_client(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        refname = request.POST.get('refname')
        refcontact = request.POST.get('refcontact')

        client= client_detail(fname=fname,lname=lname,gender=gender,contact=contact,email=email,
                      address=address,country=country,city=city,refname=refname,refcontact=refcontact)
        client.save()
        
        return redirect('client_list')
    return render(request,'client/add_client.html')

@login_required(login_url='/admin_login/')
def client_list(request):
    client = client_detail.objects.all()
    return render(request,'client/client_list.html',context={'clients':client})

@login_required(login_url='/admin_login/')
def edit_client(request,pk):
    if request.method=="POST":
        id = request.POST.get('client_id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        refname = request.POST.get('refname')
        refcontact = request.POST.get('refcontact')

        client= client_detail(id=id,fname=fname,lname=lname,gender=gender,contact=contact,email=email,
                      address=address,country=country,city=city,refname=refname,refcontact=refcontact)
        client.save()
        return redirect('client_list')
    update = client_detail.objects.get(id=pk)
    return render(request,'client/edit_client.html',context={'updates':update})


@login_required(login_url='/admin_login/')
def delete_client(request,pk):
    client_detail.objects.get(id=pk).delete()
    return redirect('client_list')


@login_required(login_url='/admin_login/')
def client_detail_page(request):
    return render(request,'client/client_view/client_detail_page.html')


@login_required(login_url='/admin_login/')
def client_cases(request):
    return render(request,'client/client_view/client_case.html')

@login_required(login_url='/admin_login/')
def client_account(request):
    return render(request,'client/client_view/client_account.html')


@login_required(login_url='/admin_login/')
def client_case_view(request):
    return render(request,'client/client_view/client_case_view.html')




# ............Client Detail End..........


# ............Case Detail Start..........

@login_required(login_url='/admin_login/')
def add_case(request):
    if request.method == "POST":
        client_name = request.POST.get('client_name')
        adovcate_name = request.POST.get('adovcate_name')
        case_type_name = request.POST.get('case_type_name')
        respondent_name = request.POST.get('respondent_name')
        case_status_name = request.POST.get('case_status_name')
        act = request.POST.get('act')
        case_no = request.POST.get('case_no')
        case_status_name= request.POST.get('case_status_name')
        next_date = request.POST.get('next_date')
        filing_no = request.POST.get('filing_no')
        filing_date = request.POST.get('filing_date')
        reg_no = request.POST.get('reg_no')
        reg_date = request.POST.get('reg_date')
        hiring_date = request.POST.get('hiring_date')
        cnr_no = request.POST.get('cnr_no')
        description = request.POST.get('description')
        police_station_name = request.POST.get('police_station_name')
        fir_no = request.POST.get('fir_no')
        fir_date = request.POST.get('fir_date')
        court_no = request.POST.get('court_no')
        court_name = request.POST.get('court_name')
        court_type_name = request.POST.get('court_type_name')
        judge_name = request.POST.get('judge_name')
        judge_type_name = request.POST.get('judge_type_name')

        case_detail(client_name=client_name,adovcate_name=adovcate_name,case_type_name=case_type_name,
                    respondent_name=respondent_name,case_status_name=case_status_name, case_no=case_no,
                    act=act,filing_no=filing_no,filing_date=filing_date,reg_no=reg_no,
                    reg_date=reg_date,hiring_date=hiring_date,cnr_no=cnr_no,
                    description=description,police_station_name=police_station_name,fir_date=fir_date,
                    fir_no=fir_no,court_no=court_no,court_name=court_name,court_type_name=court_type_name,
                    judge_name=judge_name,judge_type_name=judge_type_name,next_date=next_date).save()
        
        return redirect('case_list')
        
    client = client_detail.objects.all()
    team = team_member.objects.all()
    cas_status = case_status.objects.all()
    cas_type = case_type.objects.all()
    c_name = court.objects.all()
    c_type = court_type.objects.all()
    judge_type = judge.objects.all()
    dic = {'client_name':client,
           'team_member':team,
           'case_status':cas_status,
           'case_type':cas_type,
           'court_type':c_type,
           'court_name':c_name,
           'judge_type':judge_type
           } 
    return render(request,'case/add_case.html',context=dic)


@login_required(login_url='/admin_login/')
def case_list(request):
    case=case_detail.objects.all()
    return render(request,'case/case_list.html',context={'cases':case})


@login_required(login_url='/admin_login/')
def edit_case(request,pk):
    if request.method == "POST":
        client_id = request.POST.get('client_id')
        client_name = request.POST.get('client_name')
        adovcate_name = request.POST.get('adovcate_name')
        case_type_name = request.POST.get('case_type_name')
        respondent_name = request.POST.get('respondent_name')
        case_status_name = request.POST.get('case_status_name')
        act = request.POST.get('act')
        case_no = request.POST.get('case_no')
        case_status_name= request.POST.get('case_status_name')
        next_date = request.POST.get('next_date')
        filing_no = request.POST.get('filing_no')
        filing_date = request.POST.get('filing_date')
        reg_no = request.POST.get('reg_no')
        reg_date = request.POST.get('reg_date')
        hiring_date = request.POST.get('hiring_date')
        cnr_no = request.POST.get('cnr_no')
        description = request.POST.get('description')
        police_station_name = request.POST.get('police_station_name')
        fir_no = request.POST.get('fir_no')
        fir_date = request.POST.get('fir_date')
        court_no = request.POST.get('court_no')
        court_name = request.POST.get('court_name')
        court_type_name = request.POST.get('court_type_name')
        judge_name = request.POST.get('judge_name')
        judge_type_name = request.POST.get('judge_type_name')

        case_detail(client_name=client_name,adovcate_name=adovcate_name,case_type_name=case_type_name,
                    respondent_name=respondent_name,case_status_name=case_status_name, case_no=case_no,
                    act=act,filing_no=filing_no,filing_date=filing_date,reg_no=reg_no,
                    reg_date=reg_date,hiring_date=hiring_date,cnr_no=cnr_no,id=client_id,
                    description=description,police_station_name=police_station_name,fir_date=fir_date,
                    fir_no=fir_no,court_no=court_no,court_name=court_name,court_type_name=court_type_name,
                    judge_name=judge_name,judge_type_name=judge_type_name,next_date=next_date).save()
        
        return redirect('case_list')
    case=case_detail.objects.get(id=pk)
    client = client_detail.objects.all()
    team = team_member.objects.all()
    cas_status = case_status.objects.all()
    cas_type = case_type.objects.all()
    c_name = court.objects.all()
    c_type = court_type.objects.all()
    judge_type = judge.objects.all()
    dic = {'client_name':client,
           'cases':case,
           'team_member':team,
           'case_status':cas_status,
           'case_type':cas_type,
           'court_type':c_type,
           'court_name':c_name,
           'judge_type':judge_type
           }
    return render(request,'case/edit_case.html',context=dic)


@login_required(login_url='/admin_login/')
def delete_case(request,pk):
    case_detail.objects.get(id = pk).delete()
    return redirect('case_list')


@login_required(login_url='/admin_login/')
def view_case_transfer(request):
    return render(request,'case/view_case_transfer.html')


@login_required(login_url='/admin_login/')
def search_case(request):
    search = request.GET.get('q') 
    data = case_detail.objects.filter(case_no__icontains = search)
    return render(request,'case/search_case.html',context={'data':data})


#................Appointment start............


@login_required(login_url='/admin_login/')
def add_appoinment(request):
    if request.method=="POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        time = request.POST.get('time')

        apt=appiontment(name=name,address=address,contact=contact,date=date,time=time)
        appiontment.save(apt)
        return redirect('appointment_list')
    return render(request,'appointment/appointment_create.html')


@login_required(login_url='/admin_login/')
def appoinment_list(request):
    apt = appiontment.objects.all()
    return render(request,'appointment/appointment_list.html',context={'apt':apt})


@login_required(login_url='/admin_login/')
def delete_appoinment(request,pk):
    appiontment.objects.get(id=pk).delete()
    return redirect('appointment_list')


@login_required(login_url='/admin_login/')
def search_appoinment(request):
    search = request.GET.get('q') 
    data = appiontment.objects.filter(name__icontains = search)
    return render(request,'appointment/search_appointment.html',context={'data':data})
   
@login_required(login_url='/admin_login/')   
def edit_appoinment(request,pk):
    apt = appiontment.objects.get(id=pk)
    if request.method=="POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        time = request.POST.get('time')

        apt=appiontment(id=id,name=name,address=address,contact=contact,date=date,time=time)
        appiontment.save(apt)
        return redirect('appointment_list')
    
    return render(request,'appointment/appointment_edit.html',context={'apt':apt})
#................Appointment End............


#................Add Case Type Start............
@login_required(login_url='/admin_login/')
def add_case_type(request):
    if request.method=="POST":
        type_name = request.POST.get('name')
        discription= request.POST.get('discription')
        case_type(type_name=type_name,discription=discription).save()
        return redirect('case_type_list')
    return render(request,"case_type/add_casetype.html")

@login_required(login_url='/admin_login/')
def edit_case_type(request):
    return render(request,"case_type/edit_casetype.html")

@login_required(login_url='/admin_login/')
def delete_case_type(request,pk):
    case_type.objects.get(id=pk).delete()
    return redirect("case_type_list")

@login_required(login_url='/admin_login/')
def case_type_list(request):
    case_type_list=case_type.objects.all()
    return render(request,"case_type/casetype_list.html",context={'case_type':case_type_list})

#................Add Case Type End ............



#................Add Case status Start............
@login_required(login_url='/admin_login/')
def add_case_status(request):
    if request.method=="POST":
        status_name = request.POST.get('name')
        discription = request.POST.get('discription')

        case_status(status_name=status_name,discription=discription).save()
        return redirect("case_status_list")
    return render(request,"case_status/add_case_status.html")


@login_required(login_url='/admin_login/')
def edit_case_status(request):
    return render(request,"case_status/edit_case_status.html")


@login_required(login_url='/admin_login/')
def delete_case_status(request,pk):
    case_status.objects.get(id=pk).delete()
    return redirect("case_status_list")


@login_required(login_url='/admin_login/')
def case_status_list(request):
    status = case_status.objects.all()
    return render(request,"case_status/case_status_list.html",context={'status':status})

#................Add Case Status End ............


#................ Court Detail Start............
@login_required(login_url='/admin_login/')
def add_court(request):
    if request.method=="POST":
        court_name = request.POST.get('name')
        detail = request.POST.get('detail')

        court(court_name=court_name,detail=detail).save()
        return redirect('court_list')
    return render(request,"court/add_court.html")


@login_required(login_url='/admin_login/')
def edit_court(request):
    return render(request,"court/edit_court.html")


@login_required(login_url='/admin_login/')
def delete_court(request,pk):
    court.objects.get(id=pk).delete()
    return redirect("court_list")


@login_required(login_url='/admin_login/')
def court_list(request):
    court_list = court.objects.all()
    return render(request,"court/court_list.html",context={'court_list':court_list})

#..........Court detail End........

#..........Court Type detail Start........
@login_required(login_url='/admin_login/')
def add_court_type(request):
    if request.method=="POST":
        court_type_name=request.POST.get('name')
        detail = request.POST.get('detail')
        court_type(court_type_name=court_type_name,detail=detail).save()
        return redirect('court_type_list')
    return render(request,"court_type/add_court_type.html")


@login_required(login_url='/admin_login/')
def edit_court_type(request):
    return render(request,"court_type/edit_court_type.html")


@login_required(login_url='/admin_login/')
def delete_court_type(request,pk):
    court_type.objects.get(id=pk).delete()
    return redirect("court_type_list")


@login_required(login_url='/admin_login/')
def court_type_list(request):
    court_type_name = court_type.objects.all()
    return render(request,"court_type/court_type_list.html",context={'court_type':court_type_name})


#................Court Type Detail End ............


#..........Judge detail Start........
@login_required(login_url='/admin_login/')
def add_judge(request):
    if request.method=="POST":
        judge_name= request.POST.get('name')
        detail = request.POST.get('detail')
        judge(judge_name=judge_name,detail=detail).save()
        return redirect('judge_list')
    return render(request,"judge/add_judge.html")


@login_required(login_url='/admin_login/')
def edit_judge(request):
    return render(request,"judge/edit_judge.html")


@login_required(login_url='/admin_login/')
def delete_judge(request,pk):
    judge.objects.get(id=pk).delete()
    return redirect("judge_list")


@login_required(login_url='/admin_login/')
def judge_list(request):
    judges = judge.objects.all()
    return render(request,"judge/judge_list.html",context={'judge':judges})


#................Judge Detail End ............



#..........Tax detail Start........
@login_required(login_url='/admin_login/')
def add_tax(request):
    if request.method =="POST":
        tax_name = request.POST.get('name')
        percentage = request.POST.get('percentage')
        detail = request.POST.get('detail')
        taxes(tax_name=tax_name,percentage=percentage,detail=detail).save()
        return redirect('tax_list')
         
    return render(request,"tax/add_tax.html")


@login_required(login_url='/admin_login/')
def edit_tax(request):
    return render(request,"tax/edit_tax.html")


@login_required(login_url='/admin_login/')
def delete_tax(request,pk):
    taxes.objects.get(id = pk).delete()
    return redirect("tax_list")


@login_required(login_url='/admin_login/')
def tax_list(request):
    tax = taxes.objects.all()
    return render(request,"tax/tax_list.html",context={'taxes':tax})


#................Tax Detail End ............



#..........Services detail Start........
@login_required(login_url='/admin_login/')
def add_services(request):
    if request.method == "POST":
        service_name = request.POST.get('name')
        amount = request.POST.get('amount')
        detail = request.POST.get('detail')
        services(service_name=service_name,amount=amount,detail=detail).save()
        return redirect('services_list')
    return render(request,"service/add_services.html")


@login_required(login_url='/admin_login/')
def edit_services(request):
    return render(request,"service/edit_services.html")


@login_required(login_url='/admin_login/')
def delete_services(request,pk):
    services.objects.get(id=pk).delete()
    return redirect("services_list")


@login_required(login_url='/admin_login/')
def services_list(request):
    service=services.objects.all()
    return render(request,"service/services_list.html",context={'services':service})


#................Services Detail End ............



#..........Services detail Start........
@login_required(login_url='/admin_login/')
def add_invoice(request):
    if request.method=="POST":
        client_name = request.POST.get('client_name')
        invioce_no = request.POST.get('invioce_no')
        invioce_date = request.POST.get('invioce_date')
        service_name = request.POST.get('services_name')
        services_description = request.POST.get('services_description')
        tax_name = request.POST.get('taxes_name')
        qty = request.POST.get('qty')
        amount = request.POST.get('amount')
        due = request.POST.get('due')
        pay = request.POST.get('pay')
        total_amount = request.POST.get('total_amount')

        invioces(client_name=client_name,invioce_no=invioce_no,invioce_date=invioce_date,services_name=service_name,
                 services_description=services_description,taxes_name=tax_name,qty=qty,
                 amount=amount,due=due,pay=pay,total_amount=total_amount).save()
        return redirect('invoice_list')
    client = client_detail.objects.all()
    service = services.objects.all()
    tax = taxes.objects.all()
    dic={'clients':client,'services':service,'taxes':tax}
    return render(request,"invoice/add_invoice.html",context=dic)


@login_required(login_url='/admin_login/')
def edit_invoice(request):
    return render(request,"invoice/edit_invoice.html")


@login_required(login_url='/admin_login/')
def delete_invoice(request,pk):
    invioces.objects.get(id=pk).delete()
    return redirect('invoice_list')


@login_required(login_url='/admin_login/')
def invoice_list(request):
    invioce=invioces.objects.all()
    return render(request,"invoice/invoice_list.html",context={'invoices':invioce})


@login_required(login_url='/admin_login/')
def invoice_view(request,pk):
    view=invioces.objects.get(id=pk)
    return render(request,"invoice/invoice_view.html",context={'views':view})


@login_required(login_url='/admin_login/')
def delete_history(request,pk):
    payment.objects.get(id=pk).delete()
    return redirect('invoice_payment_history')


@login_required(login_url='/admin_login/')
def add_payment(request,pk):
    pay = invioces.objects.get(id=pk)
    if request.method=="POST":
        id = request.POST.get('invioce_id')
        invoice_no=request.POST.get('invioce_no')
        amount=request.POST.get('amount')
        method=request.POST.get('method')
        note=request.POST.get('note')
        payment(invioce_no=invoice_no,amount=amount,payment_method=method,note=note).save()

        dues = pay.total_amount - (int(amount) + pay.pay)
        pay.pay=int(amount) + pay.pay

        pay.due=dues
        if pay.pay >= pay.total_amount:
            pay.due=0
            pay.save()
        else:
            pay.save()
        return redirect('invoice_payment_history')

    return render(request,"invoice/add_payment.html",context={'payment':pay})


@login_required(login_url='/admin_login/')
def invoice_payment_history(request):
    payment_history = payment.objects.all()
    
            
    return render(request,"invoice/invoice_payment_history.html",context={'history':payment_history})



#................Services Detail End ............


#................Team Member Start............
@login_required(login_url='/admin_login/')
def team_member_list(request):
    members = team_member.objects.all() 
    return render(request,"team_member/team_member_list.html",context={'member':members})

@login_required(login_url='/admin_login/')
def add_member(request):
    if request.method =="POST":
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        profile = request.FILES.get('profile')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        password = request.POST.get('password')
        country = request.POST.get('country')
        city = request.POST.get('city')
        role = request.POST.get('role')

        add_member = team_member(fname=fname,lname=lname,profile=profile,
                                 contact=contact,email=email,address=address,
                                 zip_code=zip_code,password=password,country=country,
                                 city=city,role=role)
        add_member.save()
       
    return render(request,"team_member/add_member.html")


@login_required(login_url='/admin_login/')
def edit_member(request,pk):
    member = team_member.objects.get(id=pk)
    if request.method =="POST":
        id = request.POST.get('id')
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        profile = request.FILES.get('profile')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        password = request.POST.get('password')
        country = request.POST.get('country')
        city = request.POST.get('city')
        role = request.POST.get('role')

        edit_member = team_member(id=id,fname=fname,lname=lname,profile=profile,
                                 contact=contact,email=email,address=address,
                                 zip_code=zip_code,password=password,country=country,
                                 city=city,role=role)
        team_member.save(edit_member)
        return redirect("team_member_list")

    return render(request,"team_member/edit_member.html",context={'members':member})


@login_required(login_url='/admin_login/')
def delete_member(request,pk):
    member = team_member.objects.get(id=pk).delete()
    return redirect('team_member_list')


@login_required(login_url='/admin_login/')
def search_member(request):
    search_member = request.GET.get('search_member') 
    data = team_member.objects.filter(fname__icontains = search_member)
    return render(request,'team_member/search_member.html',context={'search':data})

#................Team Member End............

#................Acount start............


def register(request):

    if request.method == 'POST':
        Name = request.POST.get('user_name')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        
        user_obj = User.objects.create(username = Name,email = Email)
        user_obj.set_password(Password)
        user_obj.save()  
        return redirect('admin_login')    
    return render(request,'acounts/register.html')


def admin_login(request):
    if request.method =='POST':
        Name = request.POST.get('user_name')
        Password = request.POST.get('password')
        user = authenticate(username = Name,password = Password)
        request.session['name'] = Name
        if user is not None:
            login(request,user)
            return redirect('index')
            
    return render(request,'acounts/admin_login.html')

def admin_logout(request):
    request.session.clear()
    logout(request)
    return redirect('admin_login')    


#................Acount End............

