from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_message, name='chat_message'),
    path('health/', views.health_check, name='health_check'),
]