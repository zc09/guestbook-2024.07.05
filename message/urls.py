from django.urls import path
from .views import *

urlpatterns = [ 
    # message/  => 留言列表 
    path('', views.MessageList.as_view(), name='msg_list') 
    # message/1/, message/2/, ... 
    path('<int:pk>/', views MessageRead.as_view(), name='msg_view') 
    path('create/', views.MessageNew.as_view(), name='msg_create')
    ]