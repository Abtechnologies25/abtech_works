from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('nagercoil-admin-dashboard/', views.nagercoil_admin_dashboard, name='nagercoil_admin_dashboard'),
    path('chennai-admin-dashboard/', views.chennai_admin_dashboard, name='chennai_admin_dashboard'),
    path('tirunelveli-admin-dashboard/', views.tirunelveli_admin_dashboard, name='tirunelveli_admin_dashboard'),
    path('pudukottai-admin-dashboard/', views.pudukottai_admin_dashboard, name='pudukottai_admin_dashboard'),
    path('billwise-admin-dashboard/', views.billwise_admin_dashboard, name='billwise_admin_dashboard'),
    path('workstatus-admin-dashboard/', views.workstatus_admin_dashboard, name='workstatus_admin_dashboard'),

    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject-user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),

    path('phd-registration/<str:branch>/', views.phd_registration_report, name='phd_registration_report'),
    path('phd_registration/add/<str:branch>/', views.add_phd_registration, name='add_phd_registration'),
    path('phd-registration/<str:branch>/edit/<int:record_id>/', views.edit_phd_registration, name='edit_phd_registration'),
    path('phd-registration/<str:branch>/delete/<int:record_id>/', views.delete_phd_registration, name='delete_phd_registration'),
    path('project-registration/<str:branch>/', views.project_registration_report, name='project_registration_report'),
    
    # Add New Project Registration
    path('project-registration/add/<str:branch>/', views.add_project_registration, name='add_project_registration'),
    
    # Edit Project Registration
    path('project-registration/<str:branch>/edit/<int:record_id>/', views.edit_project_registration, name='edit_project_registration'),
    
    # Delete Project Registration
    path('project-registration/<str:branch>/delete/<int:record_id>/', views.delete_project_registration, name='delete_project_registration'),

    path('internship-registration/<str:branch>/', views.internship_registration_report, name='internship_registration_report'),
    path('internship-registration/add/<str:branch>/', views.add_internship_registration, name='add_internship_registration'),
    path('internship-registration/<str:branch>/edit/<int:record_id>/', views.edit_internship_registration, name='edit_internship_registration'),
    path('internship-registration/<str:branch>/delete/<int:record_id>/', views.delete_internship_registration, name='delete_internship_registration'),

    path('publication-registration/<str:branch>/', views.publication_registration_report, name='publication_registration_report'),
    path('publication-registration/add/<str:branch>/', views.add_publication_registration, name='add_publication_registration'),
    path('publication-registration/<str:branch>/edit/<int:record_id>/', views.edit_publication_registration, name='edit_publication_registration'),
    path('publication-registration/<str:branch>/delete/<int:record_id>/', views.delete_publication_registration, name='delete_publication_registration'),


    path('daily-income/<str:branch>/', views.daily_income_expenditure_report, name='daily_income_expenditure_report'),
    path('daily-income/add/<str:branch>/', views.add_daily_income_expenditure, name='add_daily_income_expenditure'),
    path('daily-income/<str:branch>/edit/<int:record_id>/', views.edit_daily_income_expenditure, name='edit_daily_income_expenditure'),
    path('daily-income/<str:branch>/delete/<int:record_id>/', views.delete_daily_income_expenditure, name='delete_daily_income_expenditure'),
    
    path('phd-registration/download/<str:branch>/', views.download_phd_report, name='download_phd_report'),
    path('project-registration/download/<str:branch>/', views.download_project_report, name='download_project_report'),
    path('internship-registration/download/<str:branch>/', views.download_internship_report, name='download_internship_report'),
    path('publication-registration/download/<str:branch>/', views.download_publication_report, name='download_publication_report'),
    path('income-expenditure/download/<str:branch>/', views.download_income_expenditure_report, name='download_income_expenditure_report'),

    path('payment-voucher/<str:branch>/', views.payment_voucher_report, name='payment_voucher_report'),
    path('payment-voucher/add/<str:branch>/', views.add_payment_voucher, name='add_payment_voucher'),
    path('payment-voucher/<str:branch>/edit/<int:record_id>/', views.edit_payment_voucher, name='edit_payment_voucher'),
    path('payment-voucher/<str:branch>/delete/<int:record_id>/', views.delete_payment_voucher, name='delete_payment_voucher'),
    path('payment-voucher/download/<str:branch>/', views.download_payment_voucher_report, name='download_payment_voucher_report'),

    path('bill-dashboard/<str:branch>/', views.billwise_dashboard, name='billwise_dashboard'),

    # List, Add, Edit, Delete per bill type
    path('billwise-payment/<str:branch>/<str:bill_type>/', views.bill_list, name='bill_list'),
    path('billwise-payment/<str:branch>/<str:bill_type>/add/', views.add_bill, name='add_bill'),
    path('billwise-payment/<str:branch>/<str:bill_type>/edit/<int:record_id>/', views.edit_bill, name='edit_bill'),
    path('billwise-payment/<str:branch>/<str:bill_type>/delete/<int:record_id>/', views.delete_bill, name='delete_bill'),
    path(
    'billwise-payment/<str:branch>/<str:bill_type>/export/',
    views.export_bills_to_excel,
    name='export_bills_to_excel'
),
    path('add-work-status/', views.add_work_status, name='add_work_status'),
    path('work-status/', views.work_status_list, name='work_status_list'),
    path('update-work-status/<int:pk>/', views.update_work_status, name='update_work_status'),
    path('delete-work-status/<int:pk>/', views.delete_work_status, name='delete_work_status'),
]
