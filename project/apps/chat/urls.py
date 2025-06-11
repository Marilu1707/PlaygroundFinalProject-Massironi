from django.urls import path
from chat.views import ver_chats, iniciar_chat, ver_chat
from chat.views import EliminarChatView

urlpatterns = [
    path('', ver_chats, name='ver_chats'),
    path('nuevo/', iniciar_chat, name='nuevo_chat'),
    path('chat/<int:id>/mensajes/', ver_chat, name='ver_chat'),
    path('chat/<int:pk>/eliminar/', EliminarChatView.as_view(), name='borrar_chat'),
]
