import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch11app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py

def choose_user_ob_ch11(request):
    if 'username' in request.session:
        from datetime import datetime

        currentMonth = datetime.now().month
        a = currentMonth - 1
        l = ['jan_rent_flag', 'feb_rent_flag', 'march_rent_flag', 'april_rent_flag', 'may_rent_flag', 'june_rent_flag',
             'july_rent_flag',
             'auguest_rent_flag', 'sept_rent_flag', 'october_rent_flag', 'nov_rent_flag', 'dec_rent_flag']
        ll = ['jan_due_amt', 'feb_due_amt', 'march_due_amt', 'april_due_amt', 'may_due_amt', 'june_due_amt',
              'july_due_amt',
              'auguest_due_amt', 'sept_due_amt', 'october_due_amt', 'nov_due_amt', 'dec_due_amt']

        d={'1':'get_total_due_feb','2':'get_total_due_march',
           '3':'get_total_due_april','4':'get_total_due_may',
           '_ob_ch11':'get_total_due_june','6':'get_total_due_july',
           '7':'get_total_due_auguest'
           }

        color=d['7']
        print('color',color)

        res = []
        res.append(l[a])
        #res.append(ll[a])

        print(res)

        from datetime import datetime
        cmm = datetime.now().month
        cm = cmm - 1
        #gtc = a[cm]

        rn = request.POST.get('rno')

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2),
            'roomno':rn,
            'room': room_pg1.objects.all().order_by('roon_no').values(),
            'res' : res,
            'a' : 1,
            '{% if i.get_total_due_auguest >0 %}' : '{% if i.get_total_due_auguest >0 %}',
        }
        return render(request, 'branches/branch11/payments/choose_user.html',context)
def payment_user_details_ob_ch11(request, id):
    if 'username' in request.session:

        r=pg1_new_guest.objects.all().filter(id=id,flag=2)
        rl=[]
        for i in r:
            rl.append(i.roon_no)
            break

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(id=id,flag=2),
            'rll' : rl,
        }
        return render(request, 'branches/branch11/payments/payment_user_details.html', context)



def close_choose_user_ob_ch11(request,id):
    if 'username' in request.session:
        from datetime import datetime

        currentMonth = datetime.now().month
        a = currentMonth - 1
        l = ['jan_rent_flag', 'feb_rent_flag', 'march_rent_flag', 'april_rent_flag', 'may_rent_flag', 'june_rent_flag',
             'july_rent_flag',
             'auguest_rent_flag', 'sept_rent_flag', 'october_rent_flag', 'nov_rent_flag', 'dec_rent_flag']
        ll = ['jan_due_amt', 'feb_due_amt', 'march_due_amt', 'april_due_amt', 'may_due_amt', 'june_due_amt',
              'july_due_amt',
              'auguest_due_amt', 'sept_due_amt', 'october_due_amt', 'nov_due_amt', 'dec_due_amt']

        d={'1':'get_total_due_feb','2':'get_total_due_march',
           '3':'get_total_due_april','4':'get_total_due_may',
           '_ob_ch11':'get_total_due_june','6':'get_total_due_july',
           '7':'get_total_due_auguest'
           }

        color=d['7']
        print('color',color)

        res = []
        res.append(l[a])
        #res.append(ll[a])

        print(res)

        from datetime import datetime
        cmm = datetime.now().month
        cm = cmm - 1
        #gtc = a[cm]

        #rn = request.POST.get('rno')
        rn=id

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2),
            'roomno':rn,
            'room': room_pg1.objects.all().order_by('roon_no').values(),
            'res' : res,
            'a' : 1,
            '{% if i.get_total_due_auguest >0 %}' : '{% if i.get_total_due_auguest >0 %}',
        }
        return render(request, 'branches/branch11/payments/choose_user.html',context)




#jan make payments start here

def monthly_jan_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.jan_rent = amt
            jp.remark = remark
            jp.jan_due_amt = due_amt
            jp.jan_dis_amt = dis_amt
            jp.jan_rent_rec_date = date
            jp.jan_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.jan_rent = amt
            jp.remark = remark
            jp.jan_due_amt = due_amt
            jp.jan_dis_amt = dis_amt
            jp.jan_rent_rec_date = date
            jp.jan_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            ll = []
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s = ''.join(l)
            gc = ''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, jan_rent_flag__gt=99, guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll': rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html', context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.june_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch11/payments/payment_details_of_months/jan/monthly_jan_make_payments.html',context)


#jan make payments start here

#feb make payments start here

def monthly_feb_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.feb_rent = amt
            jp.remark = remark
            jp.feb_due_amt = due_amt
            jp.feb_dis_amt = dis_amt
            jp.feb_rent_rec_date = date
            jp.feb_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.feb_rent = amt
            jp.remark = remark
            jp.feb_due_amt = due_amt
            jp.feb_dis_amt = dis_amt
            jp.feb_rent_rec_date = date
            jp.feb_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,feb_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2,guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.feb_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch11/payments/payment_details_of_months/feb/monthly_feb_make_payments.html', context)


#feb make payments start here

#march make payments start here

def monthly_march_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.march_rent = amt
            jp.remark = remark
            jp.march_due_amt = due_amt
            jp.march_dis_amt = dis_amt
            jp.march_rent_rec_date = date
            jp.march_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.march_rent = amt
            jp.remark = remark
            jp.march_due_amt = due_amt
            jp.march_dis_amt = dis_amt
            jp.march_rent_rec_date = date
            jp.march_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,march_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.march_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch11/payments/payment_details_of_months/march/monthly_march_make_payments.html', context)

#march make payments start here


#april make payments start here

def monthly_april_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.april_rent = amt
            jp.remark = remark
            jp.april_due_amt = due_amt
            jp.april_dis_amt = dis_amt
            jp.april_rent_rec_date = date
            jp.april_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.april_rent = amt
            jp.remark = remark
            jp.april_due_amt = due_amt
            jp.april_dis_amt = dis_amt
            jp.april_rent_rec_date = date
            jp.april_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,april_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.april_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch11/payments/payment_details_of_months/april/monthly_april_make_payments.html', context)

#april make payments start here


#may make payments start here

def monthly_may_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.may_rent = amt
            jp.remark = remark
            jp.may_due_amt = due_amt
            jp.may_dis_amt = dis_amt
            jp.may_rent_rec_date = date
            jp.may_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll',l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.may_rent = amt
            jp.remark = remark
            jp.may_due_amt = due_amt
            jp.may_dis_amt = dis_amt
            jp.may_rent_rec_date = date
            jp.may_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,may_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.may_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch11/payments/payment_details_of_months/may/monthly_may_make_payments.html', context)

#may make payments start here

#june make payments start here

def monthly_june_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.june_rent = amt
            jp.remark = remark
            jp.june_due_amt = due_amt
            jp.june_dis_amt = dis_amt
            jp.june_rent_rec_date = date
            jp.june_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.june_rent = amt
            jp.remark = remark
            jp.june_due_amt = due_amt
            jp.june_dis_amt = dis_amt
            jp.june_rent_rec_date = date
            jp.june_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,june_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2,guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.june_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch11/payments/payment_details_of_months/june/monthly_june_make_payments.html', context)


#june make payments start here



#july make payments start here

def monthly_july_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.july_rent = amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.july_rent = amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,july_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html', context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.july_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch11/payments/payment_details_of_months/july/monthly_july_make_payments.html', context)

#july make payments end here

#agu make payments start here

def monthly_aug_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.auguest_rent = amt
            jp.remark = remark
            jp.auguest_due_amt = due_amt
            jp.auguest_dis_amt = dis_amt
            jp.auguest_rent_rec_date = date
            jp.auguest_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.auguest_rent = amt
            jp.remark = remark
            jp.auguest_due_amt = due_amt
            jp.auguest_dis_amt = dis_amt
            jp.auguest_rent_rec_date = date
            jp.auguest_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,auguest_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.auguest_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch11/payments/payment_details_of_months/aug/monthly_aug_make_payments.html', context)

#aug make payments start here

#sept make payments start here

def monthly_sept_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.sept_rent = amt
            jp.remark = remark
            jp.sept_due_amt = due_amt
            jp.sept_dis_amt = dis_amt
            jp.sept_rent_rec_date = date
            jp.sept_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.sept_rent = amt
            jp.remark = remark
            jp.sept_due_amt = due_amt
            jp.sept_dis_amt = dis_amt
            jp.sept_rent_rec_date = date
            jp.sept_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,sept_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.sept_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch11/payments/payment_details_of_months/sept/monthly_sept_make_payments.html', context)

#sept make payments start here

#oct make payments start here

def monthly_oct_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            print('amt',amt)
            print('remark',remark)

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.october_rent = amt
            jp.remark = remark
            jp.october_due_amt = due_amt
            jp.october_dis_amt = dis_amt
            jp.october_rent_rec_date = date
            jp.october_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.october_rent = amt
            jp.remark = remark
            jp.october_due_amt = due_amt
            jp.october_dis_amt = dis_amt
            jp.october_rent_rec_date = date
            jp.october_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,october_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.october_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch11/payments/payment_details_of_months/oct/monthly_oct_make_payments.html', context)

#oct make payments start here

#nov make payments start here

def monthly_nov_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.nov_rent = amt
            jp.remark = remark
            jp.nov_due_amt = due_amt
            jp.nov_dis_amt = dis_amt
            jp.nov_rent_rec_date = date
            jp.nov_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.nov_rent = amt
            jp.remark = remark
            jp.nov_due_amt = due_amt
            jp.nov_dis_amt = dis_amt
            jp.nov_rent_rec_date = date
            jp.nov_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,nov_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.nov_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch11/payments/payment_details_of_months/nov/monthly_nov_make_payments.html', context)

#nov make payments start here

#dec make payments start here

def monthly_dec_make_payments_ob_ch11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch11app
            jp = branch11app.models.pg1_new_guest.objects.get(id=id)
            jp.dec_rent = amt
            jp.remark = remark
            jp.dec_due_amt = due_amt
            jp.dec_dis_amt = dis_amt
            jp.dec_rent_rec_date = date
            jp.dec_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch11app
            jp = branch11app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.dec_rent = amt
            jp.remark = remark
            jp.dec_due_amt = due_amt
            jp.dec_dis_amt = dis_amt
            jp.dec_rent_rec_date = date
            jp.dec_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,dec_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch11/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch11app
        total_discout_amt = []
        pg1_new_beds = branch11app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.dec_dis_amt))

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch11/payments/payment_details_of_months/dec/monthly_dec_make_payments.html', context)

#dec make payments start here

