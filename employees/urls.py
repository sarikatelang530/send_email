from django.urls import path
from . import views

urlpatterns = [
    path('send_birthday_emails/', views.send_birthday_emails, name='send_birthday_emails'),
    path('send_work_anniversary_emails/', views.send_work_anniversary_emails, name='send_work_anniversary_emails'),
]