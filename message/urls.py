from django.urls import path
from . import views

urlpatterns = [
    # message/  => 留言列表 
     path('', views.MassageList.as_view(), name='msg_list')   
]