from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.loginUser,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('news/',views.news,name='news'),
    path('logout',views.logoutUser,name='logout'),
    path('chat/',views.chat,name='chat'),
   # path('propli/',views.profile_phi,name='propli'),
    path('profile_philo',views.profile_philo,name='profile_philo'),
    path('prongo/',views.pro_ngo,name='prongo'),
    path('addpost/',views.add_post,name='addpost'),
    path('explore/',views.explore,name='explore'),
    #path('home/',views.home,name='home'),
    path('don_philo/',views.don_philo,name='donphilo'),
    path('addeve/',views.addevephilo,name='addeve'),
    path('newsphilo/',views.newsphilo,name='newsphilo'),
    path('eventphilo/',views.eventphilo,name='eventphilo'),
    path('payphilo/',views.payphilo,name='payphilo'),
    path('chatphilo/',views.chatphilo,name='chatphilo'),
    path('phil_up/',views.phil_up,name='philup')
]
