from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Employee, Admin, Give, Use,RECENT_MONTH_UNUSED_POINTS, MONTH_REDEMPTION, MONTH_USEAGE
from django.db.models import Sum, Count
from hashlib import sha1
import re
import datetime
from django.db.models import Q
from django.db.models.functions import ExtractMonth

def index(request):
    employee_list = Employee.objects.all()
    adminlist = Admin.objects.all()
    context = {'adminlist': adminlist, 'employee_list': employee_list}
    return render(request, 'points/index.html', context)

def login_page(request,employeeid):
    employee = Employee.objects.get(employeeid=employeeid)
    context = {'employeeid':employee.employeeid,'employeename':employee.employeename}
    print(context)
    return render(request, 'points/login_page.html', context)

def admin_login_page(request,adminid):
    admin = Admin.objects.get(adminid=adminid)
    context = {'adminid':admin.adminid, 'adminname':admin.adminname}
    print(context)
    return render(request, 'points/admin_login_page.html', context)

def give(request,employeeid):
    employee = Employee.objects.get(employeeid=employeeid)
    if int(request.POST.get('points'))>0:
        count = Give.objects.filter(givedate=datetime.date.today()).aggregate(Count('giveid'))['giveid__count']
        newid = str(datetime.date.today().strftime('%Y%m%d'))+str(count+1).zfill(3)
        reciver = Employee.objects.get(employeename=request.POST['giveto'])
        g = Give(giveid=newid,giverid=employee,reciverid=reciver,amount=request.POST['points'])
        g.save()
    givelist = Give.objects.filter(giverid=employeeid)
    recivelist = Give.objects.filter(reciverid=employeeid)
    uselist = Use.objects.filter(employeeid=employeeid)
    givesum = Give.objects.filter(giverid=employeeid).aggregate(Sum('amount'))['amount__sum']
    if givesum is None:
        givesum = 0
    recivesum = Give.objects.filter(reciverid=employeeid).aggregate(Sum('amount'))['amount__sum']
    usesum = Use.objects.filter(employeeid=employeeid).aggregate(Sum('useamount'))['useamount__sum']
    unusedpoints = recivesum + employee.initialpoints
    month = datetime.date.today().month
    Thismonthgive = \
    Give.objects.filter(giverid=employeeid).filter(givedate__month=datetime.date.today().month).aggregate(
        Sum('amount'))['amount__sum']
    if Thismonthgive is None:
        Thismonthgive = 0
    pointstogive = 1000 - Thismonthgive
    namelist = Employee.objects.all().exclude(employeeid=employeeid)
    context = {'namelist': namelist, 'month': month, 'employee': employee,
               'givelist': givelist, 'recivelist': recivelist,  'pointstogive': pointstogive, 'uselist': uselist, 'givesum': givesum,
               'recivesum': recivesum, 'unusedpoints': unusedpoints}
    return render(request, 'points/profile.html', context)

def profile(request,employeeid):
    employee = Employee.objects.get(employeeid=employeeid)
    enter = sha1(request.POST['password'].encode('utf-8')).hexdigest()
    password = Employee.objects.get(employeeid=employeeid).password
    if re.fullmatch(password,enter) is None:
        return render(request, 'points/login_page.html', {
            'employeeid': employee.employeeid,
            'employeename': employee.employeename,
            'error_message': "Wrong Password",
        })
    else:
        givelist = Give.objects.filter(giverid=employeeid)
        recivelist = Give.objects.filter(reciverid=employeeid)
        uselist = Use.objects.filter(employeeid=employeeid)
        givesum = Give.objects.filter(giverid=employeeid).aggregate(Sum('amount'))['amount__sum']
        recivesum = Give.objects.filter(reciverid=employeeid).aggregate(Sum('amount'))['amount__sum']
        usesum = Use.objects.filter(employeeid=employeeid).aggregate(Sum('useamount'))['useamount__sum']
        unusedpoints = recivesum + employee.initialpoints
        if usesum is not None:
            unusedpoints -= usesum
        month = datetime.date.today().month
        Thismonthgive = Give.objects.filter(giverid=employeeid).filter(givedate__month=datetime.date.today().month).aggregate(Sum('amount'))['amount__sum']
        if Thismonthgive is None:
            Thismonthgive = 0
        pointstogive = 1000-Thismonthgive
        namelist = Employee.objects.all().exclude(employeeid = employeeid)
        context = {'namelist':namelist,'month':month,'pointstogive':pointstogive,'employee': employee, 'givelist': givelist, 'recivelist': recivelist, 'uselist': uselist,'givesum':givesum,'recivesum':recivesum,'unusedpoints':unusedpoints}
        return render(request, 'points/profile.html', context)

def use(request,employeeid):
    employee = Employee.objects.get(employeeid=employeeid)
    count = Use.objects.filter(employeeid=employeeid).aggregate(Count('useid'))['useid__count']
    newid = str(employeeid)+str(count+1).zfill(3)
    u = Use(useid=newid, useamount=10000, employeeid=employee)
    u.save()
    givelist = Give.objects.filter(giverid=employeeid)
    recivelist = Give.objects.filter(reciverid=employeeid)
    uselist = Use.objects.filter(employeeid=employeeid)
    givesum = Give.objects.filter(giverid=employeeid).aggregate(Sum('amount'))['amount__sum']
    recivesum = Give.objects.filter(reciverid=employeeid).aggregate(Sum('amount'))['amount__sum']
    usesum = Use.objects.filter(employeeid=employeeid).aggregate(Sum('useamount'))['useamount__sum']
    unusedpoints = recivesum + employee.initialpoints - usesum
    month = datetime.date.today().month
    Thismonthgive = \
    Give.objects.filter(giverid=employeeid).filter(givedate__month=datetime.date.today().month).aggregate(
        Sum('amount'))['amount__sum']
    if Thismonthgive is None:
        Thismonthgive = 0
    pointstogive = 1000 - Thismonthgive
    namelist = Employee.objects.all().exclude(employeeid = employeeid)
    context = {'namelist':namelist,'month':month,'pointstogive':pointstogive,'employee': employee, 'givelist': givelist, 'recivelist': recivelist, 'uselist': uselist,'givesum':givesum,'recivesum':recivesum,'unusedpoints':unusedpoints}
    return render(request, 'points/profile.html', context)

def admin(request, adminid):
    admin = Admin.objects.get(adminid=adminid)
    enter = sha1(request.POST['password'].encode('utf-8')).hexdigest()
    password = Admin.objects.get(adminid=adminid).password
    if re.fullmatch(password, enter) is None:
        return render(request, 'points/admin_login_page.html', {
            'adminid':adminid,
            'adminname': admin.adminname,
            'error_message': "Wrong Password",
        })
    else:
        view = RECENT_MONTH_UNUSED_POINTS.objects.all()
        month_redemption = MONTH_REDEMPTION.objects.filter(MONTH=datetime.date.today().month)
        month_use = MONTH_USEAGE.objects.filter(Q(recivemonth=datetime.date.today().month) | Q(givemonth=datetime.date.today().month))
        #month_use = MONTH_USEAGE.objects.all()
        for m in month_use:
            print('r:',m.givemonth)
        ms = MONTH_REDEMPTION.objects.values('MONTH').distinct()
        context = {'view': view,'admin':admin,'month_redemption':month_redemption,'month_use':month_use,'ms':ms,'this_month':datetime.date.today().month,'selected_month':datetime.date.today().month}
        return render(request, 'points/admin.html', context)

def changemonth(request, adminid):
    admin = Admin.objects.get(adminid=adminid)
    view = RECENT_MONTH_UNUSED_POINTS.objects.all()
    month_redemption = MONTH_REDEMPTION.objects.filter(MONTH=request.POST['month'])
    month_use = MONTH_USEAGE.objects.filter(
        Q(recivemonth=request.POST['month']) | Q(givemonth=request.POST['month']))
    ms = MONTH_REDEMPTION.objects.values('MONTH').distinct()
    context = {'view': view, 'admin': admin, 'month_redemption': month_redemption,'month_use':month_use, 'ms': ms,'this_month':datetime.date.today().month,'selected_month':request.POST['month']}
    return render(request, 'points/admin.html', context)