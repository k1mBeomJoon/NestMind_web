from django.urls import path
from . import views

app_name = 'inquiry'

urlpatterns = [
    path('one-on-one-inquiry/', views.one_on_one_inquiry, name='one_on_one_inquiry'),
    path('inquiry-history/', views.inquiry_history, name='inquiry_history'),
] 