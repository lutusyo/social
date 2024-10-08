from django.urls import path, include
#from django.urls import reverse_lazy
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #previous log in view
    #path('login/', views.user_login, name='login'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name = 'dashboard'),
    path('edit/', views.edit, name = 'edit'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
     path('delete-account/', views.delete_account, name='delete-account'),

    #path('password_change/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='registration/password_change_form.html',
    #         success_url=reverse_lazy('password_change_done')),
    #     name='password_change'),
    #path('password_change/done/',
    #     auth_views.PasswordChangeDoneView.as_view(
    #         template_name='registration/password_change_done.html'),
    #     name='password_change_done'),



        # reset password urls
    #    path('password_reset/', auth_views.PasswordResetView.as_view(), name = "password_reset"),
    #    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    #    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    #    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name = "password_reset_complete"),


]
