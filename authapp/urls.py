
from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('workouts',views.workouts,name="workouts"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path('attendance',views.attendance,name="attendance"),
    path('checkattendance',views.checkattendance,name="checkattendance"),
    path('gallery',views.gallery,name="gallery"),
    path('gainmuscle',views.gainmuscle,name="gainmuscle"),
    path('gainstrength',views.gainstrength,name="gainstrength"),
    path('loseweight',views.loseweight,name="loseweight"),
    path('getfit',views.getfit,name="getfit"),
    path('suggest',views.suggest,name="suggest"),
    
    
]