from os import name
from django.forms.utils import ErrorList
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_sucess/', views.loginsucess, name='sucess_login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),
        name='reset_password'),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_sent.html'), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
        name='password_reset_confirm'),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'), 
        name='password_reset_complete'),

    path('cadastro/', views.cadastrar, name='cadastrar'),

]


'''
1- submit email form                         //PasswordResetView.as_view()
2- email enviado com sucesso                 //PasswordResetDoneView.as_view()
1- link do reset no email                    //PasswordResetConfirmView.as_view()
1- mensagem de alterado com sucesso          //PasswordResetCompleteView.as_view()
'''