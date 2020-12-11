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

]

