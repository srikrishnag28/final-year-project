from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('assign_user/', assign_user, name='assign_user'),
    path('profile/<str:username>/', profile, name='profile'),
    path('assign-criteria/', assign_user_to_criteria, name='assign_user_to_criteria'),
    path('delete-criteria/<str:username>/<str:criteria>/', delete_user_to_criteria, name='delete_user_to_criteria'),
]
