"""MDMproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MDMusers import views as MDMusers_views

urlpatterns = [
    path('editProfile/', MDMusers_views.editProfile, name = 'edit_profile'),
    path('admin/', admin.site.urls),
    path('register/', MDMusers_views.register, name='register'),
    path('profile/', MDMusers_views.profile, name='profile'),
    path('', auth_views.LoginView.as_view(template_name='MDMusers/login.html'), name='login'),
    path('loginpage/', auth_views.LoginView.as_view(template_name='MDMusers/loginpage.html'), name='loginpage'),
    path('logout/', auth_views.LogoutView.as_view(template_name='MDMusers/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='MDMusers/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='MDMusers/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='MDMusers/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='MDMusers/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('app/', include('MDMapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)