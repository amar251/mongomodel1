from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index-page'),
    path('loginapp/user', views.create_user,name='index-page'),
    path('loginapp/', views.login,name='login-page'),
    path('', views.index,name='index-page'),
   # path('update_counter/', name='update_counter')

]