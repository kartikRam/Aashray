from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.loginUser,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('news/',views.news,name='news'),
    path('logout',views.logoutUser,name='logout'),
    path('chat/',views.chat,name='chat')
]
