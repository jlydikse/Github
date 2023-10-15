from django.urls import path
from . import views

urlpatterns = [
    path('', views.myview),
    path('register/', views.UserRegister),
    path('login/', views.UserLogin),
    path('profile/', views.myprofile),
    path('forum/', views.forum)
    

]