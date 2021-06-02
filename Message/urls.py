from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='message-home'),
    path('list/', views.messageList, name='messages-list'),
    path('list/read/', views.readMessage, name='read-message'),
    path('unread/', views.messageListUnread, name='messages-list-unread'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new/', views.createNewMessage, name='new-message'),
    path('delete/', views.deleteMessage, name='delete-message'),
]
