from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('create-report/', views.create_report, name='create_report'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('report-view/', views.report_view, name='report_view'),
] 