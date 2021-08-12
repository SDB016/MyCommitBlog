  
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view,name="signup"),
    path('profile/<str:id>',profile, name='profile'),
    path('edit/<str:id>', update_profile, name='updateProfile'),

]
