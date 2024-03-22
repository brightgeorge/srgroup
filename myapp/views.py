from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
import datetime

# Create your views here.

def index(request):
    context={

    }
    return render(request,'index.html',context)

def login_request(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if login.objects.filter(username=username,password=password).exists():
            loginobj=login.objects.get(username=username,password=password)
            request.session['userid']=loginobj.id
            role=loginobj.role

            if role=='Admin':
                request.session['username'] = username
                us = request.session['username']

                context={
                   'user':loginobj,
                    'name': us,

                }
                return render(request,'admindashboard/adminindex.html',context)

            if role=='Branch1':
                request.session['username'] = username
                us = request.session['username']
                import myapp
                bgs = myapp.models.background_color.objects.all().filter(username=us)
                bg = myapp.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch1/branch1index.html', context)
            if role=='Branch2':
                request.session['username'] = username
                us = request.session['username']
                import branch2app
                bgs = branch2app.models.background_color.objects.all().filter(username=us)
                bg = branch2app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch2/branch1index.html', context)
            if role=='Branch3':
                request.session['username'] = username
                us = request.session['username']
                import branch3app
                bgs = branch3app.models.background_color.objects.all().filter(username=us)
                bg = branch3app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch3/branch1index.html', context)
            if role=='Branch4':
                request.session['username'] = username
                us = request.session['username']
                import branch4app
                bgs = branch4app.models.background_color.objects.all().filter(username=us)
                bg = branch4app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch4/branch1index.html', context)
            if role=='Branch5':
                request.session['username'] = username
                us = request.session['username']
                import branch5app
                bgs = branch5app.models.background_color.objects.all().filter(username=us)
                bg = branch5app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch5/branch1index.html', context)
            if role=='Branch6':
                request.session['username'] = username
                us = request.session['username']
                import branch6app
                bgs = branch6app.models.background_color.objects.all().filter(username=us)
                bg = branch6app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch6/branch1index.html', context)
            if role=='Branch7':
                request.session['username'] = username
                us = request.session['username']
                context = {
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch7/branch1index.html', context)
            if role=='Branch8':
                request.session['username'] = username
                us = request.session['username']
                context = {
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch8/branch1index.html', context)
            if role=='Branch9':
                request.session['username'] = username
                us = request.session['username']
                import branch9app
                bgs = branch9app.models.background_color.objects.all().filter(username=us)
                bg = branch9app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch9/branch1index.html', context)
            if role=='Branch10':
                request.session['username'] = username
                us = request.session['username']
                import branch10app
                bgs = branch10app.models.background_color.objects.all().filter(username=us)
                bg = branch10app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch10/branch1index.html', context)
            if role=='Branch11':
                request.session['username'] = username
                us = request.session['username']
                import branch11app
                bgs = branch11app.models.background_color.objects.all().filter(username=us)
                bg = branch11app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch11/branch1index.html', context)
            if role=='Branch12':
                request.session['username'] = username
                us = request.session['username']
                import branch12app
                bgs = branch12app.models.background_color.objects.all().filter(username=us)
                bg = branch12app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch12/branch1index.html', context)
            if role=='Branch13':
                request.session['username'] = username
                us = request.session['username']
                import branch13app
                bgs = branch13app.models.background_color.objects.all().filter(username=us)
                bg = branch13app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch13/branch1index.html', context)

            if role=='Branch14':
                request.session['username'] = username
                us = request.session['username']
                import branch14app
                bgs = branch14app.models.background_color.objects.all().filter(username=us)
                bg = branch14app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch14/branch1index.html', context)


            else:
                return render(request,'index.html',context={'user':loginobj})
        else:
            return render(request,'index.html',context={'msg':'User Name or Password Incorrect'})
    else:
        return render(request,'index.html')


def admin_dashboard(request):
    #ul = []
    #teul = login.objects.all().filter(user_flage=1)
    #ltuel = len(teul)

    #tdul = login.objects.all().filter(user_flage=0)
    #ltudl = len(tdul)

    #ul.append(ltuel)
    #ul.append(ltudl)

    us = request.session['username']

    context = {
        'name': us,
        #'yy': ul,
        #'active_user': ltuel,
        #'total_disableusers': ltudl,

        #'tg': admin_dahsboard_calculations.total_guest(),
        #'branchwise_total_guest' : admin_dahsboard_calculations.branchwise_total_guest(),
        #'tsv1': admin_dahsboard_calculations.total_vaccant_share1(),
        #'tsv2': admin_dahsboard_calculations.total_vaccant_share2(),
        #'tsv3': admin_dahsboard_calculations.total_vaccant_share3(),
        #'tsv4': admin_dahsboard_calculations.total_vaccant_share4(),
        #'tsv5': admin_dahsboard_calculations.total_vaccant_share5(),
        #'tsv6': admin_dahsboard_calculations.total_vaccant_share6(),
        #'total_vaccant_room': admin_dahsboard_calculations.total_vaccant_room(),

        #'grand_total_collection': admin_dahsboard_calculations.total_gtc(),
        #'total_collection_advance' : admin_dahsboard_calculations.total_advance(),
        #'total_discount': admin_dahsboard_calculations.total_discount(),

        #'total_colatable_amount' : admin_dahsboard_calculations.all_total_collatable_amount(),
        #'total_collected_amount' : admin_dahsboard_calculations.all_total_collected_amount(),
        #'total_due' : admin_dahsboard_calculations.all_total_due(),
    }
    return render (request,'admindashboard/adminindex.html',context)

def admin_home(request):
    if 'username' in request.session:
        ul = []
        teul = login.objects.all().filter(user_flage=1)
        ltuel = len(teul)

        tdul = login.objects.all().filter(user_flage=0)
        ltudl = len(tdul)

        ul.append(ltuel)
        ul.append(ltudl)

        us = request.session['username']

        context = {
            'name': us,
            'yy': ul,
            'active_user': ltuel,
            'total_disableusers': ltudl,

            'tg': admin_dahsboard_calculations.total_guest(),
            # 'branchwise_total_guest' : admin_dahsboard_calculations.branchwise_total_guest(),
            'tsv1': admin_dahsboard_calculations.total_vaccant_share1(),
            'tsv2': admin_dahsboard_calculations.total_vaccant_share2(),
            'tsv3': admin_dahsboard_calculations.total_vaccant_share3(),
            'tsv4': admin_dahsboard_calculations.total_vaccant_share4(),
            'tsv5': admin_dahsboard_calculations.total_vaccant_share5(),
            'tsv6': admin_dahsboard_calculations.total_vaccant_share6(),
            'total_vaccant_room': admin_dahsboard_calculations.total_vaccant_room(),

            'grand_total_collection': admin_dahsboard_calculations.total_gtc(),
            'total_collection_advance': admin_dahsboard_calculations.total_advance(),
            'total_discount': admin_dahsboard_calculations.total_discount(),

            'total_colatable_amount': admin_dahsboard_calculations.all_total_collatable_amount(),
            'total_collected_amount': admin_dahsboard_calculations.all_total_collected_amount(),
            'total_due': admin_dahsboard_calculations.all_total_due(),
        }
        return render(request,'admindashboard/admin_home.html',context)
    return render(request,'index.html')

#************USER SECTION STARTED HERE ***************

def view_all_users(request):
    if 'username' in request.session:
        vu=login.objects.filter(user_flage=1)
        context={
            'users':vu
        }
        return render(request,'admindashboard/users/view_all_users.html',context)
    return render(request,'index.html')

def create_user(request):
    if 'username' in request.session:
        return render(request,'admindashboard/users/user_creation.html')
    return render(request, 'index.html')

def user_regi(request):
    itname = request.POST.get('username')
    chkitemname = login.objects.filter(username=itname).exists()
    print('this is m y test uname',chkitemname)
    empcod= request.POST.get('code')
    chkemcod= login.objects.filter(emp_id=empcod).exists()
    print('this is m y test user code', chkemcod)
    if chkitemname == True or chkemcod == True:
        if chkitemname == True and chkemcod == True:
            messages.info(request, 'User name and Employee Code both are already exists!. please try another one')
        if chkitemname == False and chkemcod == True:
            messages.info(request, 'Employee Code already exists!. please try another one')
        if chkitemname == True and chkemcod == False:
            messages.info(request, 'User name already exists!. please try another one')
        return render(request, 'admindashboard/users/user_creation.html', )
    else:
        if request.method == 'POST':
            ucode=request.POST.get('code')
            empname = request.POST.get('name')
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            urole = request.POST.get('role')
            empbranch = request.POST.get('branch')

            udes = request.POST.get('description')
            fl = request.POST.get('eanable_disable')
            chk = 11
            if fl == None:
                chk = 0
            else:
                chk = 1
            uc=login()
            uc.emp_id = ucode
            uc.emp_name = empname
            uc.username = uname
            uc.password = upass
            uc.role = urole
            uc.emp_branch=empbranch

            uc.emp_description=udes
            uc.user_flage = chk
            uc.save()

    messages.info(request,'user created sucessfully')
    context = {
        'users': login.objects.filter(user_flage=1),
    }
    return render(request,'admindashboard/users/view_all_users.html',context)

def delete_user(request,id):
    if 'username' in request.session:
        de=login.objects.get(id=id)
        de.delete()
        messages.info(request, 'user deleted sucessfully')
        vu = login.objects.all()
        context = {
            'users': login.objects.filter(user_flage=1),
            'users': vu
        }
        return render(request, 'admindashboard/users/view_all_users.html', context)
    return render(request, 'index.html')

def user_update(request,id):
    if request.method == 'POST':
        ucode = request.POST.get('code')
        empname = request.POST.get('name')
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        urole = request.POST.get('role')

        udes = request.POST.get('description')
        fl = request.POST.get('eanable_disable')
        chk = 11
        if fl == None:
            chk = 0
        else:
            chk = 1
        uc = login.objects.get(id=id)
        uc.emp_id = ucode
        uc.emp_name = empname
        uc.username = uname
        uc.password = upass
        uc.role = urole

        uc.emp_description = udes
        uc.user_flage = chk
        uc.save()
        messages.info(request, 'user updated sucessfully')
        return view_all_users(request)

    context = {
        'users': login.objects.filter(user_flage=1),
        'sd': login.objects.get(id=id),
    }
    return render(request,'admindashboard/users/update_user.html',context)

#************USER SECTION END HERE ***************

def select_branch(request):
    return render(request, 'admindashboard/branches/select_branch.html')

#logout
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request,'index.html')