from django.urls import path
from . import views


urlpatterns = [
    path("", views.chat_page, name="ai_chat_page"),
    path("chat/", views.chat, name="ai_chat"),
]