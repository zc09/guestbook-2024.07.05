from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,DeleteView
from .models import Message

# Create your views here.
class MassageList(ListView):
    model = Message

    # 頁面範本檔案名稱: 應用程式/資料模型_list.html => messsage/message_list.html
    # 頁面範本變數: 名稱資料模型_list => message_list

    class MessageRead(DetailView):
        model = Message

    # 頁面範本檔案名稱: 應用程式/資料模型_detail.html => messsage/detail_list.html
    # 頁面範本變數名稱: 名稱資料模型_list => message

class MessageNew(CreateView):
    model = Message
    fields = ['user','receipt','subject','content']
    success_url = '/message/'
    # fields = '__all__'

     # 頁面範本檔案名稱: 應用程式/資料模型_form.html => messsage/message_form.html