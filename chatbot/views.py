import os

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Chat

import sys
sys.path.append("..")

from qa import send_user


# Create your views here.
def chatbot(request):
    chats = Chat.objects.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        answer, wiki_extract = send_user.send_user(message)

        chat = Chat(message=message, response=answer, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': answer})
    return render(request, 'chatbot.html', {'chats': chats})
