from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_choice, name='login'),
    path('login_real/', views.login_real, name='login_real'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('check-duplicate/', views.check_duplicate, name='check_duplicate'),
    path('change-nickname/', views.change_nickname, name='change_nickname'),
    path('change-password/', views.change_password, name='change_password'),
    path('withdraw/', views.withdraw, name='withdraw'),
]