from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employeeid>/login_page', views.login_page, name='login_page'),
    path('<int:adminid>/admin_login_page', views.admin_login_page, name='admin_login_page'),
    path('<int:employeeid>/profile', views.profile, name='profile'),
    path('<int:employeeid>/give', views.give, name='give'),
    path('<int:employeeid>/use', views.use, name='use'),
    path('<int:adminid>/admin', views.admin, name='admin'),
    path('<int:adminid>/changemonth', views.changemonth, name='admin'),
]