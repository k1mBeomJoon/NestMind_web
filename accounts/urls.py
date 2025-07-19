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
]