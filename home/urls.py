from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name='home'),
    path('foodtips/',views.tipsview, name='foodtips'),
    path('signin/',views.signinview, name='signin'),
    path('signup/',views.signupview, name='signup'),
    path('profile/',views.profileview,name='profile'),
    path('logout/',views.handlelogout),
    path('aboutus/',views.aboutview,name="aboutus"),
    path('healthblog/',views.healthblogview, name='healthblog'),
    path('foodblog',views.foodblogview, name='foodblog'),
    path('ourteam/',views.teamview,name='ourteam'),
    path('fullhealthblog/<slug:slug>/', views.fullhealthblog, name='fullhealthblog'),
    path('fullfoodblog/<slug:slug>/', views.fullfoodblog, name='fullfoodblog'),
    path('privacypolicy/',views.privacypolicy,name='privacypolicy') 
    
]
