from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,DeleteView
from .models import Message
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MessageList(ListView):
    model = Message

    # 頁面範本檔案名稱: 應用程式/資料模型_list.html => messsage/message_list.html
    # 頁面範本變數: 名稱資料模型_list => message_list

    class MessageView(DetailView):
        model = Message
        ordering = ['-created',]

    # 頁面範本檔案名稱: 應用程式/資料模型_detail.html => messsage/detail_list.html
    # 頁面範本變數名稱: 名稱資料模型_list => message

class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['user','receipt','subject','content']
    success_url = reverse_lazy('msg_list')
    # fields = '__all__'

     # 頁面範本檔案名稱: 應用程式/資料模型_form.html => messsage/message_form.html
     # 頁面範本變數名稱:form
    
    class MessageDelete(LoginRequiredMixin, DeleteView):
        model = Message
        success_url = reverse_lazy('msg_list')

    # 頁面範本檔案名稱: 應用程式/資料模型_confirm_delete.html => messsage/message_confirm.html
    # 頁面範本變數名稱:form, object,資料模型(小寫)