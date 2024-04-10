
from django import views
from django.urls import path
from case import views 

urlpatterns = [
    path('admin_login/',views.admin_login,name = 'admin_login'),
    path('index/',views.index,name = 'index'),
    
    #case Detail
    path('add_case/',views.add_case,name = 'add_case'),
    path('case_list/',views.case_list,name = 'case_list'),
    path('edit_case/<pk>/',views.edit_case,name = 'edit_case'),
    path('delete_case/<pk>/',views.delete_case,name = 'delete_case'),
    path('search_case/',views.search_case,name = 'search_case'),
    
    #Client
    path('add_client/',views.add_client,name = 'add_client'),
    path('delete_client/<pk>/',views.delete_client,name = 'delete_client'),
    path('client_list/',views.client_list,name = 'client_list'),
    path('edit_client/<pk>/',views.edit_client,name = 'edit_client'),
    path('client_cases/',views.client_cases,name = 'client_cases'),
    path('client_account/',views.client_account,name = 'client_account'),
    path('client_case_view/',views.client_case_view,name = 'client_case_view'),
    path('client_detail_page/',views.client_detail_page,name = 'client_detail_page'),

    

   
   
    #appiontment
    path('add_appointment/',views.add_appoinment,name = 'add_appointment'),
    path('appointment_list/',views.appoinment_list,name = 'appointment_list'),
    path('edit_appointment/<pk>/',views.edit_appoinment,name = 'edit_appointment'),
    path('delete_appointment/<pk>/',views.delete_appoinment,name = 'delete_appointment'),
    path('search_appointment/',views.search_appoinment,name = 'search_appointment'),
    
    #add Case Type
    path('add_case_type/',views.add_case_type,name='add_case_type'),
    path('edit_case_type/',views.edit_case_type,name='edit_case_type'),
    path('case_type_list/',views.case_type_list,name='case_type_list'),
    path('delete_case_type/<pk>/',views.delete_case_type,name='delete_case_type'),

    #add case Status
    path('add_case_status/',views.add_case_status,name='add_case_status'),
    path('edit_case_status/',views.edit_case_status,name='edit_case_status'),
    path('case_status_list/',views.case_status_list,name='case_status_list'),
    path('delete_case_status/<pk>/',views.delete_case_status,name='delete_case_status'),

    #court Detail
    path('add_court/',views.add_court,name='add_court'),
    path('edit_court/',views.edit_court,name='edit_court'),
    path('court_list/',views.court_list,name='court_list'),
    path('delete_court/<pk>/',views.delete_court,name='delete_court'),

    #Court Type Detail
    path('add_court_type/',views.add_court_type,name='add_court_type'),
    path('edit_court_type/',views.edit_court_type,name='edit_court_type'),
    path('delete_court_type/<pk>/',views.delete_court_type,name='delete_court_type'),
    path('court_type_list/',views.court_type_list,name='court_type_list'),

    
    #Judge Detail
    path('add_judge/',views.add_judge,name='add_judge'),
    path('edit_judge/',views.edit_judge,name='edit_judge'),
    path('delete_judge/<pk>/',views.delete_judge,name='delete_judge'),
    path('judge_list/',views.judge_list,name='judge_list'),


    #Services Detail
    path('add_services/',views.add_services,name='add_services'),
    path('edit_services/',views.edit_services,name='edit_services'),
    path('delete_services/<pk>/',views.delete_services,name='delete_services'),
    path('services_list/',views.services_list,name='services_list'),

    
    #Invoice Detail
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('edit_invoice/',views.edit_invoice,name='edit_invoice'),
    path('delete_invoice/<pk>/',views.delete_invoice,name='delete_invoice'),
    path('invoice_list/',views.invoice_list,name='invoice_list'),
    path('invoice_view/<pk>/',views.invoice_view,name='invoice_view'),
    path('add_payment/<pk>/',views.add_payment,name='add_payment'),
    path('delete_history/<pk>/',views.delete_history,name='delete_history'),
    path('invoice_payment_history/',views.invoice_payment_history,name='invoice_payment_history'),

    #Team Member
    path('team_member_list/',views.team_member_list,name='team_member_list'),
    path('add_member/',views.add_member,name='add_member'),
    path('edit_member/<pk>/',views.edit_member,name='edit_member'),
    path('delete_member/<pk>/',views.delete_member,name='delete_member'),
    path('search_member/',views.search_member,name='search_member'),
    
    #Taxes
    path('add_tax/',views.add_tax,name = 'add_tax'),
    path('edit_tax/',views.edit_tax,name = 'edit_tax'),
    path('delete_tax/<pk>/',views.delete_tax,name = 'delete_tax'),
    path('tax_list/',views.tax_list,name = 'tax_list'),


    #Acounts
    
    path('admin_logout/',views.admin_logout,name = 'admin_logout'),
    
    path('register/',views.register,name = 'register'),
]
