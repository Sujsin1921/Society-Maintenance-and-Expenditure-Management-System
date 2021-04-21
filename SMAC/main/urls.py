from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Home',views.Home,name='home'),
    path('Member',views.Member,name='Member'),
    path('Expences',views.Expences,name='Expences'),
    path('Collection',views.Collection,name='Collection'),
    path('Pending',views.Pending,name='Pending'),
    path('Funds',views.Funds,name='Funds'),
    path('login', views.handeLogin, name="login"),
    path('logout', views.handelLogout, name="logout"),
    path('addmember',views.addmember,name="addmember"),
    path('addinvoice',views.addinvoice,name="addinvoice"),
    path('edit',views.edit,name='edit'),
    path('delete',views.delete,name="delete"),
    path('delinv',views.delinv,name="delinv"),
    path('specialfunds',views.specialfunds,name='specialfunds'),
    path('festivefunds',views.festivefunds,name='festivefunds'),
    path('emergencefunds',views.emergencefunds,name='emergencefunds'),
    path('deleted',views.deleted,name='deleted')
]
