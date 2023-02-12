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
    path('propli_up',views.propli_up,name='propli_up'),
    path('prongo/',views.pro_ngo,name='prongo'),
    path('addpost/',views.add_post,name='addpost'),
    path('explore/',views.explore,name='explore')
]
