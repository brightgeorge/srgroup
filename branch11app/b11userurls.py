from django.urls import path, include

from . import admin_branch11
from . import admin_branch11
from . import branch11
from . import reports11
from . import payment11
from . import admin_dashboard_calculations_br11
from . import accounts11

urlpatterns = [

    path('branch1_dashboard_ob_ch11/', branch11.branch1_dashboard_ob_ch11, name='branch1_dashboard_ob_ch11'),
    path('background_ob_ch11',branch11.background_ob_ch11,name='background_ob_ch11'),
    path('background_regi_ob_ch11',branch11.background_regi_ob_ch11,name='background_regi_ob_ch11'),
    path('custom_background_regi_ob_ch11',branch11.custom_background_regi_ob_ch11,name='custom_background_regi_ob_ch11'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch11/',admin_branch11.branch1_room_create_regi_ob_ch11,name='branch1_room_create_regi_ob_ch11'),
    path('view_all_room_ob_ch11/',admin_branch11.view_all_room_ob_ch11,name='view_all_room_ob_ch11'),
    path('delete_room_ob_ch11/<id>',admin_branch11.delete_room_ob_ch11,name='delete_room_ob_ch11'),

    path('branch1_room_create_ob_ch11/',admin_branch11.branch1_room_create_ob_ch11,name='branch1_room_create_ob_ch11'),

    path('multiple_branch1_room_create_regi11/',admin_branch11.multiple_branch1_room_create_regi11,name='multiple_branch1_room_create_regi11'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch11/', admin_branch11.pg1_bed_create_regi_ob_ch11, name='pg1_bed_create_regi_ob_ch11'),
    path('pg1_view_all_beds_ob_ch11/', admin_branch11.pg1_view_all_beds_ob_ch11, name='pg1_view_all_beds_ob_ch11'),
    path('delete_bed_ob_ch11/<id>', admin_branch11.delete_bed_ob_ch11, name='delete_bed_ob_ch11'),

    path('pg1_bed_create_ob_ch11/', admin_branch11.pg1_bed_create_ob_ch11, name='pg1_bed_create_ob_ch11'),

    path('single_pg1_bed_create_regi_ob_ch11/',admin_branch11.single_pg1_bed_create_regi_ob_ch11,name='single_pg1_bed_create_regi_ob_ch11'),
    path('update_bed_basic_details_ob_ch11/<id>',admin_branch11.update_bed_basic_details_ob_ch11, name='update_bed_basic_details_ob_ch11'),

    path('multiple_single_pg1_bed_create_regi11/',admin_branch11.multiple_single_pg1_bed_create_regi11,name='multiple_single_pg1_bed_create_regi11'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch11/<id>',branch11.br1_admit_guest_ob_ch11,name='br1_admit_guest_ob_ch11'),
    path('view_all_new_guest_ob_ch11/',branch11.view_all_new_guest_ob_ch11,name='view_all_new_guest_ob_ch11'),
    path('update_br1_admit_guest_ob_ch11/<id>',branch11.update_br1_admit_guest_ob_ch11,name='update_br1_admit_guest_ob_ch11'),
    path('vacate_br1_guest_ob_ch11/<id>',branch11.vacate_br1_guest_ob_ch11,name='vacate_br1_guest_ob_ch11'),

    path('active_guest_details_ob_ch11/<guest_code>',branch11.active_guest_details_ob_ch11,name='active_guest_details_ob_ch11'),
    path('view_all_guest_ob_ch11/',branch11.view_all_guest_ob_ch11,name='view_all_guest_ob_ch11'),
    path('shift_guest_ob_ch11/<id>',branch11.shift_guest_ob_ch11,name='shift_guest_ob_ch11'),
    path('shift_guest_regi_ob_ch11/',branch11.shift_guest_regi_ob_ch11,name='shift_guest_regi_ob_ch11'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('multiple_br1_admit_guest11/<id>',branch11.multiple_br1_admit_guest11,name='multiple_br1_admit_guest11'),

#guest end here


##################################
#_ADVANCE_ob_ch11 START HERE
################################


    path('choose_months_advance_ob_ch11/',branch11.choose_months_advance_ob_ch11,name='choose_months_advance_ob_ch11'),

    path('jan_advance_ob_ch11/', branch11.jan_advance_ob_ch11, name='jan_advance_ob_ch11'),
    path('jan_make_payments_advance_ob_ch11/<id>', branch11.jan_make_payments_advance_ob_ch11,name='jan_make_payments_advance_ob_ch11'),
    path('feb_advance_ob_ch11/', branch11.feb_advance_ob_ch11, name='feb_advance_ob_ch11'),
    path('feb_make_payments_advance_ob_ch11/<id>', branch11.feb_make_payments_advance_ob_ch11,name='feb_make_payments_advance_ob_ch11'),
    path('march_advance_ob_ch11/', branch11.march_advance_ob_ch11, name='march_advance_ob_ch11'),
    path('march_make_payments_advance_ob_ch11/<id>', branch11.march_make_payments_advance_ob_ch11,name='march_make_payments_advance_ob_ch11'),
    path('april_advance_ob_ch11/', branch11.april_advance_ob_ch11, name='april_advance_ob_ch11'),
    path('april_make_payments_advance_ob_ch11/<id>', branch11.april_make_payments_advance_ob_ch11, name='april_make_payments_advance_ob_ch11'),

    path('may_advance_ob_ch11/',branch11.may_advance_ob_ch11,name='may_advance_ob_ch11'),
    path('may_make_payments_advance_ob_ch11/<id>', branch11.may_make_payments_advance_ob_ch11, name='may_make_payments_advance_ob_ch11'),
    path('june_advance_ob_ch11/',branch11.june_advance_ob_ch11,name='june_advance_ob_ch11'),
    path('june_make_payments_advance_ob_ch11/<id>', branch11.june_make_payments_advance_ob_ch11, name='june_make_payments_advance_ob_ch11'),
    path('july_advance_ob_ch11/',branch11.july_advance_ob_ch11,name='july_advance_ob_ch11'),
    path('july_make_payments_advance_ob_ch11/<id>', branch11.july_make_payments_advance_ob_ch11, name='july_make_payments_advance_ob_ch11'),
    path('auguest_advance_ob_ch11/', branch11.auguest_advance_ob_ch11, name='auguest_advance_ob_ch11'),
    path('auguest_make_payments_advance_ob_ch11/<id>', branch11.auguest_make_payments_advance_ob_ch11, name='auguest_make_payments_advance_ob_ch11'),

    path('sept_advance_ob_ch11/', branch11.sept_advance_ob_ch11, name='sept_advance_ob_ch11'),
    path('sept_make_payments_advance_ob_ch11/<id>', branch11.sept_make_payments_advance_ob_ch11,name='sept_make_payments_advance_ob_ch11'),
    path('october_advance_ob_ch11/', branch11.october_advance_ob_ch11, name='october_advance_ob_ch11'),
    path('october_make_payments_advance_ob_ch11/<id>', branch11.october_make_payments_advance_ob_ch11, name='october_make_payments_advance_ob_ch11'),
    path('nov_advance_ob_ch11/', branch11.nov_advance_ob_ch11, name='nov_advance_ob_ch11'),
    path('nov_make_payments_advance_ob_ch11/<id>', branch11.nov_make_payments_advance_ob_ch11,name='nov_make_payments_advance_ob_ch11'),
    path('dec_advance_ob_ch11/', branch11.dec_advance_ob_ch11, name='dec_advance_ob_ch11'),
    path('dec_make_payments_advance_ob_ch11/<id>', branch11.dec_make_payments_advance_ob_ch11, name='dec_make_payments_advance_ob_ch11'),



##################################
#_ADVANCE_ob_ch11 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch11/',branch11.choose_months_ob_ch11,name='choose_months_ob_ch11'),

    path('jan_ob_ch11/',branch11.jan_ob_ch11,name='jan_ob_ch11'),
    path('jan_manke_payments_ob_ch11/<id>',branch11.jan_manke_payments_ob_ch11,name='jan_manke_payments_ob_ch11'),

    path('feb_ob_ch11/',branch11.feb_ob_ch11,name='feb_ob_ch11'),
    path('feb_manke_payments_ob_ch11/<id>',branch11.feb_manke_payments_ob_ch11,name='feb_manke_payments_ob_ch11'),

    path('march_ob_ch11/',branch11.march_ob_ch11,name='march_ob_ch11'),
    path('march_manke_payments_ob_ch11/<id>',branch11.march_manke_payments_ob_ch11,name='march_manke_payments_ob_ch11'),

    path('april_ob_ch11/',branch11.april_ob_ch11,name='april_ob_ch11'),
    path('april_make_payments_ob_ch11/<id>',branch11.april_make_payments_ob_ch11,name='april_make_payments_ob_ch11'),

    path('may_ob_ch11/',branch11.may_ob_ch11,name='may_ob_ch11'),
    path('may_make_payments_ob_ch11/<id>',branch11.may_make_payments_ob_ch11,name='may_make_payments_ob_ch11'),

    path('june_ob_ch11/',branch11.june_ob_ch11,name='june_ob_ch11'),
    path('june_make_payments_ob_ch11/<id>',branch11.june_make_payments_ob_ch11,name='june_make_payments_ob_ch11'),

    path('july_ob_ch11/',branch11.july_ob_ch11,name='july_ob_ch11'),
    path('july_make_payments_ob_ch11/<id>',branch11.july_make_payments_ob_ch11,name='july_make_payments_ob_ch11'),

    path('aug_ob_ch11/',branch11.aug_ob_ch11,name='aug_ob_ch11'),
    path('aug_make_payments_ob_ch11/<id>',branch11.aug_make_payments_ob_ch11,name='aug_make_payments_ob_ch11'),

    path('sept_ob_ch11/',branch11.sept_ob_ch11,name='sept_ob_ch11'),
    path('sept_make_payments_ob_ch11/<id>',branch11.sept_make_payments_ob_ch11,name='sept_make_payments_ob_ch11'),

    path('oct_ob_ch11/',branch11.oct_ob_ch11,name='oct_ob_ch11'),
    path('oct_make_payments_ob_ch11/<id>',branch11.oct_make_payments_ob_ch11,name='oct_make_payments_ob_ch11'),

    path('nov_ob_ch11/',branch11.nov_ob_ch11,name='nov_ob_ch11'),
    path('nov_make_payments_ob_ch11/<id>',branch11.nov_make_payments_ob_ch11,name='nov_make_payments_ob_ch11'),

    path('dec_ob_ch11/',branch11.dec_ob_ch11,name='dec_ob_ch11'),
    path('dec_make_payments_ob_ch11/<id>',branch11.dec_make_payments_ob_ch11,name='dec_make_payments_ob_ch11'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch11/', payment11.choose_user_ob_ch11, name='choose_user_ob_ch11'),
    path('payment_user_details_ob_ch11/<id>', payment11.payment_user_details_ob_ch11, name='payment_user_details_ob_ch11'),
    path('close_choose_user_ob_ch11/<id>',payment11.close_choose_user_ob_ch11,name='close_choose_user_ob_ch11'),

    path('monthly_jan_make_payments_ob_ch11/<id>', payment11.monthly_jan_make_payments_ob_ch11, name='monthly_jan_make_payments_ob_ch11'),
    path('monthly_feb_make_payments_ob_ch11/<id>', payment11.monthly_feb_make_payments_ob_ch11, name='monthly_feb_make_payments_ob_ch11'),
    path('monthly_march_make_payments_ob_ch11/<id>', payment11.monthly_march_make_payments_ob_ch11, name='monthly_march_make_payments_ob_ch11'),
    path('monthly_april_make_payments_ob_ch11/<id>', payment11.monthly_april_make_payments_ob_ch11, name='monthly_april_make_payments_ob_ch11'),
    path('monthly_may_make_payments_ob_ch11/<id>', payment11.monthly_may_make_payments_ob_ch11, name='monthly_may_make_payments_ob_ch11'),
    path('monthly_june_make_payments_ob_ch11/<id>', payment11.monthly_june_make_payments_ob_ch11, name='monthly_june_make_payments_ob_ch11'),

    path('monthly_july_make_payments_ob_ch11/<id>', payment11.monthly_july_make_payments_ob_ch11, name='monthly_july_make_payments_ob_ch11'),
    path('monthly_aug_make_payments_ob_ch11/<id>', payment11.monthly_aug_make_payments_ob_ch11, name='monthly_aug_make_payments_ob_ch11'),
    path('monthly_sept_make_payments_ob_ch11/<id>', payment11.monthly_sept_make_payments_ob_ch11, name='monthly_sept_make_payments_ob_ch11'),
    path('monthly_oct_make_payments_ob_ch11/<id>', payment11.monthly_oct_make_payments_ob_ch11, name='monthly_oct_make_payments_ob_ch11'),
    path('monthly_nov_make_payments_ob_ch11/<id>', payment11.monthly_nov_make_payments_ob_ch11, name='monthly_nov_make_payments_ob_ch11'),
    path('monthly_dec_make_payments_ob_ch11/<id>', payment11.monthly_dec_make_payments_ob_ch11, name='monthly_dec_make_payments_ob_ch11'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch11/',branch11.unpaid_rent_choose_months_ob_ch11,name='unpaid_rent_choose_months_ob_ch11'),

    path('jan_unpaid_rent_ob_ch11/', branch11.jan_unpaid_rent_ob_ch11, name='jan_unpaid_rent_ob_ch11'),
    path('table_jan_unpaid_rent_ob_ch11/', branch11.table_jan_unpaid_rent_ob_ch11, name='table_jan_unpaid_rent_ob_ch11'),
    path('feb_unpaid_rent_ob_ch11/', branch11.feb_unpaid_rent_ob_ch11, name='feb_unpaid_rent_ob_ch11'),
    path('table_feb_unpaid_rent_ob_ch11/', branch11.table_feb_unpaid_rent_ob_ch11, name='table_feb_unpaid_rent_ob_ch11'),
    path('mar_unpaid_rent_ob_ch11/', branch11.mar_unpaid_rent_ob_ch11, name='mar_unpaid_rent_ob_ch11'),
    path('table_mar_unpaid_rent_ob_ch11/', branch11.table_mar_unpaid_rent_ob_ch11, name='table_mar_unpaid_rent_ob_ch11'),
    path('april_unpaid_rent_ob_ch11/', branch11.april_unpaid_rent_ob_ch11, name='april_unpaid_rent_ob_ch11'),
    path('table_april_unpaid_rent_ob_ch11/', branch11.table_april_unpaid_rent_ob_ch11, name='table_april_unpaid_rent_ob_ch11'),

    path('may_unpaid_rent_ob_ch11/', branch11.may_unpaid_rent_ob_ch11, name='may_unpaid_rent_ob_ch11'),
    path('table_may_unpaid_rent_ob_ch11/', branch11.table_may_unpaid_rent_ob_ch11, name='table_may_unpaid_rent_ob_ch11'),
    path('june_unpaid_rent_ob_ch11/', branch11.june_unpaid_rent_ob_ch11, name='june_unpaid_rent_ob_ch11'),
    path('table_june_unpaid_rent_ob_ch11/', branch11.table_june_unpaid_rent_ob_ch11, name='table_june_unpaid_rent_ob_ch11'),
    path('july_unpaid_rent_ob_ch11/', branch11.july_unpaid_rent_ob_ch11, name='july_unpaid_rent_ob_ch11'),
    path('table_july_unpaid_rent_ob_ch11',branch11.table_july_unpaid_rent_ob_ch11,name='table_july_unpaid_rent_ob_ch11'),
    path('aug_unpaid_rent_ob_ch11/', branch11.aug_unpaid_rent_ob_ch11, name='aug_unpaid_rent_ob_ch11'),
    path('table_aug_unpaid_rent_ob_ch11/',branch11.table_aug_unpaid_rent_ob_ch11,name='table_aug_unpaid_rent_ob_ch11'),

    path('sept_unpaid_rent_ob_ch11/', branch11.sept_unpaid_rent_ob_ch11, name='sept_unpaid_rent_ob_ch11'),
    path('table_sept_unpaid_rent_ob_ch11/', branch11.table_sept_unpaid_rent_ob_ch11, name='table_sept_unpaid_rent_ob_ch11'),
    path('oct_unpaid_rent_ob_ch11/', branch11.oct_unpaid_rent_ob_ch11, name='oct_unpaid_rent_ob_ch11'),
    path('table_oct_unpaid_rent_ob_ch11/', branch11.table_oct_unpaid_rent_ob_ch11, name='table_oct_unpaid_rent_ob_ch11'),
    path('nov_unpaid_rent_ob_ch11/', branch11.nov_unpaid_rent_ob_ch11, name='nov_unpaid_rent_ob_ch11'),
    path('table_nov_unpaid_rent_ob_ch11/', branch11.table_nov_unpaid_rent_ob_ch11, name='table_nov_unpaid_rent_ob_ch11'),
    path('dec_unpaid_rent_ob_ch11/', branch11.dec_unpaid_rent_ob_ch11, name='dec_unpaid_rent_ob_ch11'),
    path('table_dec_unpaid_rent_ob_ch11/', branch11.table_dec_unpaid_rent_ob_ch11, name='table_dec_unpaid_rent_ob_ch11'),

    path('details_of_unpaid_guests_ob_ch11/<id>',branch11.details_of_unpaid_guests_ob_ch11,name='details_of_unpaid_guests_ob_ch11'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch11/',branch11.paid_rent_choose_months_ob_ch11,name='paid_rent_choose_months_ob_ch11'),
    path('partially_paid_guest_choose_months_ob_ch11/',reports11.partially_paid_guest_choose_months_ob_ch11,name='partially_paid_guest_choose_months_ob_ch11'),

    path('jan_paid_rent_ob_ch11/', branch11.jan_paid_rent_ob_ch11, name='jan_paid_rent_ob_ch11'),
    path('table_jan_paid_rent_ob_ch11/', branch11.table_jan_paid_rent_ob_ch11, name='table_jan_paid_rent_ob_ch11'),
    path('jan_full_paid_guest_ob_ch11/', reports11.jan_full_paid_guest_ob_ch11, name='jan_full_paid_guest_ob_ch11'),
    path('jan_partially_paid_guest_ob_ch11/', reports11.jan_partially_paid_guest_ob_ch11, name='jan_partially_paid_guest_ob_ch11'),
    path('table_jan_partially_paid_guest_ob_ch11/', reports11.table_jan_partially_paid_guest_ob_ch11,name='table_jan_partially_paid_guest_ob_ch11'),

    path('feb_paid_rent_ob_ch11/', branch11.feb_paid_rent_ob_ch11, name='feb_paid_rent_ob_ch11'),
    path('table_feb_paid_rent_ob_ch11/', branch11.table_feb_paid_rent_ob_ch11, name='table_feb_paid_rent_ob_ch11'),
    path('feb_full_paid_guest_ob_ch11/', reports11.feb_full_paid_guest_ob_ch11, name='feb_full_paid_guest_ob_ch11'),
    path('feb_partially_paid_guest_ob_ch11/', reports11.feb_partially_paid_guest_ob_ch11, name='feb_partially_paid_guest_ob_ch11'),
    path('table_feb_partially_paid_guest_ob_ch11/', reports11.table_feb_partially_paid_guest_ob_ch11,name='table_feb_partially_paid_guest_ob_ch11'),

    path('mar_paid_rent_ob_ch11/', branch11.mar_paid_rent_ob_ch11, name='mar_paid_rent_ob_ch11'),
    path('table_mar_paid_rent_ob_ch11/', branch11.table_mar_paid_rent_ob_ch11, name='table_mar_paid_rent_ob_ch11'),
    path('march_full_paid_guest_ob_ch11/', reports11.march_full_paid_guest_ob_ch11, name='march_full_paid_guest_ob_ch11'),
    path('march_partially_paid_guest_ob_ch11/', reports11.march_partially_paid_guest_ob_ch11, name='march_partially_paid_guest_ob_ch11'),
    path('table_march_partially_paid_guest_ob_ch11/', reports11.table_march_partially_paid_guest_ob_ch11,name='table_march_partially_paid_guest_ob_ch11'),

    path('april_paid_rent_ob_ch11/', branch11.april_paid_rent_ob_ch11, name='april_paid_rent_ob_ch11'),
    path('table_april_paid_rent_ob_ch11/', branch11.table_april_paid_rent_ob_ch11, name='table_april_paid_rent_ob_ch11'),
    path('april_full_paid_guest_ob_ch11/', reports11.april_full_paid_guest_ob_ch11, name='april_full_paid_guest_ob_ch11'),
    path('april_partially_paid_guest_ob_ch11/', reports11.april_partially_paid_guest_ob_ch11, name='april_partially_paid_guest_ob_ch11'),
    path('table_april_partially_paid_guest_ob_ch11/', reports11.table_april_partially_paid_guest_ob_ch11,name='table_april_partially_paid_guest_ob_ch11'),

    path('may_paid_rent_ob_ch11/', branch11.may_paid_rent_ob_ch11, name='may_paid_rent_ob_ch11'),
    path('table_may_paid_rent_ob_ch11/', branch11.table_may_paid_rent_ob_ch11, name='table_may_paid_rent_ob_ch11'),
    path('may_full_paid_guest_ob_ch11/', reports11.may_full_paid_guest_ob_ch11, name='may_full_paid_guest_ob_ch11'),
    path('may_partially_paid_guest_ob_ch11/', reports11.may_partially_paid_guest_ob_ch11, name='may_partially_paid_guest_ob_ch11'),
    path('table_may_partially_paid_guest_ob_ch11/', reports11.table_may_partially_paid_guest_ob_ch11, name='table_may_partially_paid_guest_ob_ch11'),

    path('june_paid_rent_ob_ch11/', branch11.june_paid_rent_ob_ch11, name='june_paid_rent_ob_ch11'),
    path('table_june_paid_rent_ob_ch11/', branch11.table_june_paid_rent_ob_ch11, name='table_june_paid_rent_ob_ch11'),
    path('june_full_paid_guest_ob_ch11/', reports11.june_full_paid_guest_ob_ch11, name='june_full_paid_guest_ob_ch11'),
    path('june_partially_paid_guest_ob_ch11/', reports11.june_partially_paid_guest_ob_ch11, name='june_partially_paid_guest_ob_ch11'),
    path('table_june_partially_paid_guest_ob_ch11/', reports11.table_june_partially_paid_guest_ob_ch11, name='table_june_partially_paid_guest_ob_ch11'),

    path('july_paid_rent_ob_ch11/', branch11.july_paid_rent_ob_ch11, name='july_paid_rent_ob_ch11'),
    path('table_july_paid_rent_ob_ch11/', branch11.table_july_paid_rent_ob_ch11, name='table_july_paid_rent_ob_ch11'),
    path('july_full_paid_guest_ob_ch11/', reports11.july_full_paid_guest_ob_ch11, name='july_full_paid_guest_ob_ch11'),
    path('july_partially_paid_guest_ob_ch11/', reports11.july_partially_paid_guest_ob_ch11, name='july_partially_paid_guest_ob_ch11'),
    path('table_july_partially_paid_guest_ob_ch11/', reports11.table_july_partially_paid_guest_ob_ch11, name='table_july_partially_paid_guest_ob_ch11'),

    path('aug_paid_rent_ob_ch11/', branch11.aug_paid_rent_ob_ch11, name='aug_paid_rent_ob_ch11'),
    path('table_aug_paid_rent_ob_ch11/', branch11.table_aug_paid_rent_ob_ch11, name='table_aug_paid_rent_ob_ch11'),
    path('auguest_full_paid_guest_ob_ch11/', reports11.auguest_full_paid_guest_ob_ch11, name='auguest_full_paid_guest_ob_ch11'),
    path('auguest_partially_paid_guest_ob_ch11/', reports11.auguest_partially_paid_guest_ob_ch11,name='auguest_partially_paid_guest_ob_ch11'),
    path('table_auguest_partially_paid_guest_ob_ch11/', reports11.table_auguest_partially_paid_guest_ob_ch11,name='table_auguest_partially_paid_guest_ob_ch11'),

    path('sept_paid_rent_ob_ch11/', branch11.sept_paid_rent_ob_ch11, name='sept_paid_rent_ob_ch11'),
    path('table_sept_paid_rent_ob_ch11/', branch11.table_sept_paid_rent_ob_ch11, name='table_sept_paid_rent_ob_ch11'),
    path('sept_full_paid_guest_ob_ch11/', reports11.sept_full_paid_guest_ob_ch11, name='sept_full_paid_guest_ob_ch11'),
    path('sept_partially_paid_guest_ob_ch11/', reports11.sept_partially_paid_guest_ob_ch11, name='sept_partially_paid_guest_ob_ch11'),
    path('table_sept_partially_paid_guest_ob_ch11/', reports11.table_sept_partially_paid_guest_ob_ch11,name='table_sept_partially_paid_guest_ob_ch11'),

    path('oct_paid_rent_ob_ch11/', branch11.oct_paid_rent_ob_ch11, name='oct_paid_rent_ob_ch11'),
    path('table_oct_paid_rent_ob_ch11/', branch11.table_oct_paid_rent_ob_ch11, name='table_oct_paid_rent_ob_ch11'),
    path('october_full_paid_guest_ob_ch11/', reports11.october_full_paid_guest_ob_ch11, name='october_full_paid_guest_ob_ch11'),
    path('october_partially_paid_guest_ob_ch11/', reports11.october_partially_paid_guest_ob_ch11,name='october_partially_paid_guest_ob_ch11'),
    path('table_october_partially_paid_guest_ob_ch11/', reports11.table_october_partially_paid_guest_ob_ch11,name='table_october_partially_paid_guest_ob_ch11'),

    path('nov_paid_rent_ob_ch11/', branch11.nov_paid_rent_ob_ch11, name='nov_paid_rent_ob_ch11'),
    path('table_nov_paid_rent_ob_ch11/', branch11.table_nov_paid_rent_ob_ch11, name='table_nov_paid_rent_ob_ch11'),
    path('nov_full_paid_guest_ob_ch11/', reports11.nov_full_paid_guest_ob_ch11, name='nov_full_paid_guest_ob_ch11'),
    path('nov_partially_paid_guest_ob_ch11/', reports11.nov_partially_paid_guest_ob_ch11, name='nov_partially_paid_guest_ob_ch11'),
    path('table_nov_partially_paid_guest_ob_ch11/', reports11.table_nov_partially_paid_guest_ob_ch11,name='table_nov_partially_paid_guest_ob_ch11'),

    path('dec_paid_rent_ob_ch11/', branch11.dec_paid_rent_ob_ch11, name='dec_paid_rent_ob_ch11'),
    path('table_dec_paid_rent_ob_ch11/', branch11.table_dec_paid_rent_ob_ch11, name='table_dec_paid_rent_ob_ch11'),
    path('dec_full_paid_guest_ob_ch11/', reports11.dec_full_paid_guest_ob_ch11, name='dec_full_paid_guest_ob_ch11'),
    path('dec_partially_paid_guest_ob_ch11/', reports11.dec_partially_paid_guest_ob_ch11, name='dec_partially_paid_guest_ob_ch11'),
    path('table_dec_partially_paid_guest_ob_ch11/', reports11.table_dec_partially_paid_guest_ob_ch11,name='table_dec_partially_paid_guest_ob_ch11'),

    path('details_of_paid_guests_ob_ch11/<id>',branch11.details_of_paid_guests_ob_ch11,name='details_of_paid_guests_ob_ch11'),
    path('full_paid_guest_ob_ch11/',reports11.full_paid_guest_ob_ch11,name='full_paid_guest_ob_ch11'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch11/',branch11.viewall_vacate_guest_ob_ch11,name='viewall_vacate_guest_ob_ch11'),
    path('details_of_vacate_guest_ob_ch11/<id>',branch11.details_of_vacate_guest_ob_ch11,name='details_of_vacate_guest_ob_ch11'),
    path('full_vacated_guest_details_ob_ch11',branch11.full_vacated_guest_details_ob_ch11,name='full_vacated_guest_details_ob_ch11'),
    path('full_vacated_guest_table_ob_ch11',branch11.full_vacated_guest_table_ob_ch11,name='full_vacated_guest_table_ob_ch11'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch11/<id>', branch11.jan_manke_payments_vacate_ob_ch11, name='jan_manke_payments_vacate_ob_ch11'),
    path('feb_manke_payments_vacate_ob_ch11/<id>', branch11.feb_manke_payments_vacate_ob_ch11, name='feb_manke_payments_vacate_ob_ch11'),
    path('march_manke_payments_vacate_ob_ch11/<id>', branch11.march_manke_payments_vacate_ob_ch11, name='march_manke_payments_vacate_ob_ch11'),
    path('april_make_payments_vacate_ob_ch11/<id>', branch11.april_make_payments_vacate_ob_ch11, name='april_make_payments_vacate_ob_ch11'),

    path('may_make_payments_vacate_ob_ch11/<id>', branch11.may_make_payments_vacate_ob_ch11, name='may_make_payments_vacate_ob_ch11'),
    path('june_make_payments_vacate_ob_ch11/<id>', branch11.june_make_payments_vacate_ob_ch11, name='june_make_payments_vacate_ob_ch11'),
    path('july_make_payments_vacate_ob_ch11/<id>', branch11.july_make_payments_vacate_ob_ch11, name='july_make_payments_vacate_ob_ch11'),
    path('aug_make_payments_vacate_ob_ch11/<id>', branch11.aug_make_payments_vacate_ob_ch11, name='aug_make_payments_vacate_ob_ch11'),

    path('sept_make_payments_vacate_ob_ch11/<id>', branch11.sept_make_payments_vacate_ob_ch11, name='sept_make_payments_vacate_ob_ch11'),
    path('oct_make_payments_vacate_ob_ch11/<id>', branch11.oct_make_payments_vacate_ob_ch11, name='oct_make_payments_vacate_ob_ch11'),
    path('nov_make_payments_vacate_ob_ch11/<id>', branch11.nov_make_payments_vacate_ob_ch11, name='nov_make_payments_vacate_ob_ch11'),
    path('dec_make_payments_vacate_ob_ch11/<id>', branch11.dec_make_payments_vacate_ob_ch11, name='dec_make_payments_vacate_ob_ch11'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch11/',branch11.detail_guest_general_ob_ch11,name='detail_guest_general_ob_ch11'),

    path('jan_print_ob_ch11/',branch11.jan_print_ob_ch11,name='jan_print_ob_ch11'),
    path('feb_print_ob_ch11/',branch11.feb_print_ob_ch11,name='feb_print_ob_ch11'),
    path('march_print_ob_ch11/',branch11.march_print_ob_ch11,name='march_print_ob_ch11'),
    path('april_print_ob_ch11/',branch11.april_print_ob_ch11,name='april_print_ob_ch11'),

    path('may_print_ob_ch11/',branch11.may_print_ob_ch11,name='may_print_ob_ch11'),
    path('june_print_ob_ch11/',branch11.june_print_ob_ch11,name='june_print_ob_ch11'),
    path('july_print_ob_ch11/', branch11.july_print_ob_ch11, name='july_print_ob_ch11'),
    path('aug_print_ob_ch11/', branch11.aug_print_ob_ch11, name='aug_print_ob_ch11'),

    path('sept_print_ob_ch11/', branch11.sept_print_ob_ch11, name='sept_print_ob_ch11'),
    path('oct_print_ob_ch11/', branch11.oct_print_ob_ch11, name='oct_print_ob_ch11'),
    path('nov_print_ob_ch11/', branch11.nov_print_ob_ch11, name='nov_print_ob_ch11'),
    path('dec_print_ob_ch11/', branch11.dec_print_ob_ch11, name='dec_print_ob_ch11'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch11/', branch11.jan_close_ob_ch11, name='jan_close_ob_ch11'),
    path('jan_close_decision_page_ob_ch11/', branch11.jan_close_decision_page_ob_ch11, name='jan_close_decision_page_ob_ch11'),
    path('feb_close/', branch11.feb_close_ob_ch11, name='feb_close_ob_ch11'),
    path('feb_close_decision_page_ob_ch11/', branch11.feb_close_decision_page_ob_ch11, name='feb_close_decision_page_ob_ch11'),
    path('mar_close_ob_ch11/', branch11.mar_close_ob_ch11, name='mar_close_ob_ch11'),
    path('mar_close_decision_page/', branch11.mar_close_decision_page_ob_ch11, name='mar_close_decision_page_ob_ch11'),
    path('apr_close_ob_ch11/', branch11.apr_close_ob_ch11, name='apr_close_ob_ch11'),
    path('apr_close_decision_page_ob_ch11/', branch11.apr_close_decision_page_ob_ch11, name='apr_close_decision_page_ob_ch11'),

    path('may_close_ob_ch11/', branch11.may_close_ob_ch11, name='may_close_ob_ch11'),
    path('may_close_decision_page_ob_ch11/', branch11.may_close_decision_page_ob_ch11, name='may_close_decision_page_ob_ch11'),
    path('jun_close_ob_ch11/', branch11.jun_close_ob_ch11, name='jun_close_ob_ch11'),
    path('jun_close_decision_page_ob_ch11/', branch11.jun_close_decision_page_ob_ch11, name='jun_close_decision_page_ob_ch11'),
    path('jul_close_ob_ch11/', branch11.jul_close_ob_ch11, name='jul_close_ob_ch11'),
    path('jul_close_decision_page_ob_ch11/', branch11.jul_close_decision_page_ob_ch11, name='jul_close_decision_page_ob_ch11'),
    path('aug_close_ob_ch11/', branch11.aug_close_ob_ch11, name='aug_close_ob_ch11'),
    path('aug_close_decision_page_ob_ch11/', branch11.aug_close_decision_page_ob_ch11, name='aug_close_decision_page_ob_ch11'),

    path('sep_close_ob_ch11/', branch11.sep_close_ob_ch11, name='sep_close_ob_ch11'),
    path('sep_close_decision_page_ob_ch11/', branch11.sep_close_decision_page_ob_ch11, name='sep_close_decision_page_ob_ch11'),
    path('oct_close_ob_ch11/', branch11.oct_close_ob_ch11, name='oct_close_ob_ch11'),
    path('oct_close_decision_page_ob_ch11/', branch11.oct_close_decision_page_ob_ch11, name='oct_close_decision_page_ob_ch11'),
    path('nov_close_ob_ch11/', branch11.nov_close_ob_ch11, name='nov_close_ob_ch11'),
    path('nov_close_decision_page_ob_ch11/', branch11.nov_close_decision_page_ob_ch11, name='nov_close_decision_page_ob_ch11'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch11/',reports11.detailed_report_choose_months_ob_ch11,name='detailed_report_choose_months_ob_ch11'),

    path('jan_details_live_ob_ch11/', reports11.jan_details_live_ob_ch11, name='jan_details_live_ob_ch11'),
    path('jan_print_live_ob_ch11/', reports11.jan_print_live_ob_ch11, name='jan_print_live_ob_ch11'),
    path('feb_details_live_ob_ch11/', reports11.feb_details_live_ob_ch11, name='feb_details_live_ob_ch11'),
    path('feb_print_live_ob_ch11/', reports11.feb_print_live_ob_ch11, name='feb_print_live_ob_ch11'),
    path('march_details_live_ob_ch11/', reports11.march_details_live_ob_ch11, name='march_details_live_ob_ch11'),
    path('march_print_live_ob_ch11/', reports11.march_print_live_ob_ch11, name='march_print_live_ob_ch11'),

    path('april_details_live_ob_ch11/', reports11.april_details_live_ob_ch11, name='april_details_live_ob_ch11'),
    path('april_print_live_ob_ch11/', reports11.april_print_live_ob_ch11, name='april_print_live_ob_ch11'),
    path('may_details_live_ob_ch11/', reports11.may_details_live_ob_ch11, name='may_details_live_ob_ch11'),
    path('may_print_live_ob_ch11/', reports11.may_print_live_ob_ch11, name='may_print_live_ob_ch11'),
    path('june_details_live_ob_ch11/',reports11.june_details_live_ob_ch11,name='june_details_live_ob_ch11'),
    path('june_print_live_ob_ch11/', reports11.june_print_live_ob_ch11, name='june_print_live_ob_ch11'),

    path('july_details_live_ob_ch11/', reports11.july_details_live_ob_ch11, name='july_details_live_ob_ch11'),
    path('july_print_live_ob_ch11/', reports11.july_print_live_ob_ch11, name='july_print_live_ob_ch11'),
    path('auguest_details_live_ob_ch11/', reports11.auguest_details_live_ob_ch11, name='auguest_details_live_ob_ch11'),
    path('auguest_print_live_ob_ch11/', reports11.auguest_print_live_ob_ch11, name='auguest_print_live_ob_ch11'),
    path('sept_details_live_ob_ch11/', reports11.sept_details_live_ob_ch11, name='sept_details_live_ob_ch11'),
    path('sept_print_live_ob_ch11/', reports11.sept_print_live_ob_ch11, name='sept_print_live_ob_ch11'),

    path('october_details_live_ob_ch11/', reports11.october_details_live_ob_ch11, name='october_details_live_ob_ch11'),
    path('october_print_live_ob_ch11/', reports11.october_print_live_ob_ch11, name='october_print_live_ob_ch11'),
    path('nov_details_live_ob_ch11/', reports11.nov_details_live_ob_ch11, name='nov_details_live_ob_ch11'),
    path('nov_print_live_ob_ch11/', reports11.nov_print_live_ob_ch11, name='nov_print_live_ob_ch11'),
    path('dec_details_live_ob_ch11/', reports11.dec_details_live_ob_ch11, name='dec_details_live_ob_ch11'),
    path('dec_print_live_ob_ch11/', reports11.dec_print_live_ob_ch11, name='dec_print_live_ob_ch11'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch11/', reports11.viewall_vaccant_room_ob_ch11, name='viewall_vaccant_room_ob_ch11'),

    path('d_ob_ch11/', branch11.dynamic, name='dynamic'),

    path('manage_bed_ob_ch11/', branch11.manage_bed_ob_ch11, name='manage_bed_ob_ch11'),
    path('manage_new_guest_ob_ch11/', branch11.manage_new_guest_ob_ch11, name='manage_new_guest_ob_ch11'),
    path('manage_update_new_guest_ob_ch11/<id>', branch11.manage_update_new_guest_ob_ch11, name='manage_update_new_guest_ob_ch11'),
    path('manage_update_beds_ob_ch11/<id>', branch11.manage_update_beds_ob_ch11, name='manage_update_beds_ob_ch11'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch11/', branch11.view_all_due_amt_ob_ch11, name='view_all_due_amt_ob_ch11'),
    path('due_amt_mgt_choose_months_ob_ch11/', branch11.due_amt_mgt_choose_months_ob_ch11, name='due_amt_mgt_choose_months_ob_ch11'),

    path('view_jan_account_details_ob_ch11/', branch11.view_jan_account_details_ob_ch11, name='view_jan_account_details_ob_ch11'),
    path('jan_account_mgt_ob_ch11/<id>',branch11.jan_account_mgt_ob_ch11,name='jan_account_mgt_ob_ch11'),
    path('view_feb_account_details_ob_ch11/', branch11.view_feb_account_details_ob_ch11, name='view_feb_account_details_ob_ch11'),
    path('feb_account_mgt_ob_ch11/<id>',branch11.feb_account_mgt_ob_ch11,name='feb_account_mgt_ob_ch11'),
    path('view_march_account_details_ob_ch11/', branch11.view_march_account_details_ob_ch11, name='view_march_account_details_ob_ch11'),
    path('march_account_mgt_ob_ch11/<id>',branch11.march_account_mgt_ob_ch11,name='march_account_mgt_ob_ch11'),
    path('view_april_account_details_ob_ch11/', branch11.view_april_account_details_ob_ch11, name='view_april_account_details_ob_ch11'),
    path('april_account_mgt_ob_ch11/<id>',branch11.april_account_mgt_ob_ch11,name='april_account_mgt_ob_ch11'),

    path('view_may_account_details_ob_ch11/',branch11.view_may_account_details_ob_ch11,name='view_may_account_details_ob_ch11'),
    path('may_account_mgt_ob_ch11/<id>', branch11.may_account_mgt_ob_ch11, name='may_account_mgt_ob_ch11'),
    path('view_june_account_details_ob_ch11/', branch11.view_june_account_details_ob_ch11, name='view_june_account_details_ob_ch11'),
    path('june_account_mgt_ob_ch11/<id>',branch11.june_account_mgt_ob_ch11,name='june_account_mgt_ob_ch11'),
    path('view_july_account_details_ob_ch11/', branch11.view_july_account_details_ob_ch11, name='view_july_account_details_ob_ch11'),
    path('july_account_mgt_ob_ch11/<id>',branch11.july_account_mgt_ob_ch11,name='july_account_mgt_ob_ch11'),
    path('view_auguest_account_details_ob_ch11/', branch11.view_auguest_account_details_ob_ch11, name='view_auguest_account_details_ob_ch11'),
    path('auguest_account_mgt_ob_ch11/<id>',branch11.auguest_account_mgt_ob_ch11,name='auguest_account_mgt_ob_ch11'),

    path('view_sept_account_details_ob_ch11/', branch11.view_sept_account_details_ob_ch11, name='view_sept_account_details_ob_ch11'),
    path('sept_account_mgt_ob_ch11/<id>',branch11.sept_account_mgt_ob_ch11,name='sept_account_mgt_ob_ch11'),
    path('view_october_account_details_ob_ch11/', branch11.view_october_account_details_ob_ch11, name='view_october_account_details_ob_ch11'),
    path('october_account_mgt_ob_ch11/<id>',branch11.october_account_mgt_ob_ch11,name='october_account_mgt_ob_ch11'),
    path('view_nov_account_details_ob_ch11/', branch11.view_nov_account_details_ob_ch11, name='view_nov_account_details_ob_ch11'),
    path('nov_account_mgt_ob_ch11/<id>',branch11.nov_account_mgt_ob_ch11,name='nov_account_mgt_ob_ch11'),
    path('view_dec_account_details_ob_ch11/', branch11.view_dec_account_details_ob_ch11, name='view_dec_account_details_ob_ch11'),
    path('dec_account_mgt_ob_ch11/<id>',branch11.dec_account_mgt_ob_ch11,name='dec_account_mgt_ob_ch11'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch11', admin_dashboard_calculations_br11.monthly_details_due_ob_ch11, name='monthly_details_due_ob_ch11'),
    path('monthly_collection_details_ob_ch11/', admin_dashboard_calculations_br11.monthly_collection_details_ob_ch11, name='monthly_collection_details_ob_ch11'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch11/',branch11.guest_all_ob_ch11,name='guest_all_ob_ch11'),



#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category11/', accounts11.view_all_category11, name='view_all_category11'),
    path('create_new_category11/', accounts11.create_new_category11, name='create_new_category11'),
    path('regi_new_category11/', accounts11.regi_new_category11, name='regi_new_category11'),
    path('update_category11/<id>',accounts11.update_category11,name='update_category11'),

    path('delete_category11/<id>', accounts11.delete_category11, name='delete_category11'),
    path('view_all_category_delete11/', accounts11.view_all_category_delete11, name='view_all_category_delete11'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items11/', accounts11.view_all_items11, name='view_all_items11'),
    path('create_new_item11/', accounts11.create_new_item11, name='create_new_item11'),
    path('regi_new_item11/', accounts11.regi_new_item11, name='regi_new_item11'),
    path('delete_item11/<id>',accounts11.delete_item11,name='delete_item11'),
    path('update_item11/<id>', accounts11.update_item11, name='update_item11'),
    path('view_all_items_delete11/',accounts11.view_all_items_delete11,name='view_all_items_delete11'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger11/', accounts11.view_all_ledger11, name='view_all_ledger11'),
    path('create_new_ledger11/', accounts11.create_new_ledger11, name='create_new_ledger11'),
    path('regi_new_ledger11/', accounts11.regi_new_ledger11, name='regi_new_ledger11'),
    path('delete_ledger11/<id>',accounts11.delete_ledger11,name='delete_ledger11'),
    path('update_ledger11/<id>',accounts11.update_ledger11,name='update_ledger11'),
    path('view_all_ledger_delete11/',accounts11.view_all_ledger_delete11,name='view_all_ledger_delete11'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book11/', accounts11.view_all_accounts_book11, name='view_all_accounts_book11'),
    path('create_new_accounts_book11/', accounts11.create_new_accounts_book11, name='create_new_accounts_book11'),
    path('regi_new_accounts_book11/', accounts11.regi_new_accounts_book11, name='regi_new_accounts_book11'),
    path('update_accounts_book11/<id>',accounts11.update_accounts_book11,name='update_accounts_book11'),
    path('delete_accounts_book11/<id>',accounts11.delete_accounts_book11,name='delete_accounts_book11'),
    path('view_all_accounts_book_delete11/',accounts11.view_all_accounts_book_delete11,name='view_all_accounts_book_delete11'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries11/', accounts11.get_countries11, name='get_countries11'),

    path('in_exp_items_entry11/', accounts11.in_exp_items_entry11, name='in_exp_items_entry11'),
    path('reg_in_exp_items_entry11/', accounts11.reg_in_exp_items_entry11, name='reg_in_exp_items_entry11'),
    path('delete_journal11/<id>',accounts11.delete_journal11,name='delete_journal11'),
    path('update_in_exp_items_entry11/<id>',accounts11.update_in_exp_items_entry11,name='update_in_exp_items_entry11'),
    path('detailed_journal_report11/',accounts11.detailed_journal_report11,name='detailed_journal_report11'),
    path('journal_report_deleted11/',accounts11.journal_report_deleted11,name='journal_report_deleted11'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise11/', accounts11.daily_category_wise11, name='daily_category_wise11'),
    path('monthly_category_based_reports11/',accounts11.monthly_category_based_reports11,name='monthly_category_based_reports11'),
    path('yearly_category_based_reports11/', accounts11.yearly_category_based_reports11,name='yearly_category_based_reports11'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed11/', accounts11.daily_detailed11, name='daily_detailed11'),
    path('monthly_detailed11/',accounts11.monthly_detailed11,name='monthly_detailed11'),
    path('yearly_detailed11/',accounts11.yearly_detailed11,name='yearly_detailed11'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports11/', accounts11.item_based_reports11, name='item_based_reports11'),
    path('daily_item_based_reports11/',accounts11.daily_item_based_reports11,name='daily_item_based_reports11'),
    path('monthly_item_based_reports11/',accounts11.monthly_item_based_reports11,name='monthly_item_based_reports11'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports11/', accounts11.ledger_based_reports11, name='ledger_based_reports11'),
    path('monthly_ledger_based_reports11/', accounts11.monthly_ledger_based_reports11, name='monthly_ledger_based_reports11'),
    path('daily_ledger_based_reports11/',accounts11.daily_ledger_based_reports11,name='daily_ledger_based_reports11'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports11/', accounts11.accounts_book_based_reports11, name='accounts_book_based_reports11'),
    path('daily_accounts_book_based_reports11/',accounts11.daily_accounts_book_based_reports11,name='daily_accounts_book_based_reports11'),
    path('monthly_accounts_book_based_reports11/',accounts11.monthly_accounts_book_based_reports11,name='monthly_accounts_book_based_reports11'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months11/', accounts11.monthly_reports_choose_months11, name='monthly_reports_choose_months11'),
    path('monthly_detailed_daily_in_exp_items_report11/<mo>',accounts11.monthly_detailed_daily_in_exp_items_report11,name='monthly_detailed_daily_in_exp_items_report11'),

    path('single_monthly_reports_choose_months11/', accounts11.single_monthly_reports_choose_months11,name='single_monthly_reports_choose_months11'),
    path('single_monthly_daily_in_exp_items_report11/<mo>',accounts11.single_monthly_daily_in_exp_items_report11,name='single_monthly_daily_in_exp_items_report11'),

    path('accounts_dash_board_ob_ch11/',accounts11.accounts_dash_board_ob_ch11,name='accounts_dash_board_ob_ch11'),

    path('profit_sharing_choose_months11', accounts11.profit_sharing_choose_months11,name='profit_sharing_choose_months11'),
    path('profit_sharing11/<mo>', accounts11.profit_sharing11, name='profit_sharing11'),
    path('view_share_holders11', accounts11.view_share_holders11, name='view_share_holders11'),
    path('create_share_holders11', accounts11.create_share_holders11, name='create_share_holders11'),
    path('regi_share_holders11', accounts11.regi_share_holders11, name='regi_share_holders11'),
    path('update_share_holders11/<id>', accounts11.update_share_holders11, name='update_share_holders11'),
    path('delete_share_holders11/<id>', accounts11.delete_share_holders11, name='delete_share_holders11'),
    path('view_deleted_share_holders11', accounts11.view_deleted_share_holders11, name='view_deleted_share_holders11'),

]