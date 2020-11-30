from django.contrib import admin
from django.urls import path, include
from gym.views import *

urlpatterns = [
    path('', Index, name='home'),
    path('about', About, name='about'),
    path('contact', Contact, name='contact'),
    path('admin_login', Login, name='login'),
    path('logout', Logout_admin, name='logout'),
    path('add_enquiry', Add_Enquiry, name='add_enquiry'),
    path('view_enquiry', View_Enquiry, name='view_enquiry'),
    path('add_plan', Add_Plan, name='add_plan'),
    path('view_plan', View_Plan, name='view_plan'),
    path('add_equipment', Add_Equipment, name='add_equipment'),
    path('view_equipment', View_Equipment, name='view_equipment'),
    path('delete_enquiry(?p<int:pid>)', Delete_Enquiry, name='delete_enquiry'),
    path('delete_plan(?p<int:pid>)', Delete_Plan, name='delete_plan'),
    path('delete_equipment(?p<int:pid>)', Delete_Equipment, name='delete_equipment'),

]