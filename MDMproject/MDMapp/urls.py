from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('enroll/', views.enroll, name="enroll"),
    path('userview/', views.user_info, name="userview"),
    path('cellview/', views.cellphone_info, name="cellview"),

]
