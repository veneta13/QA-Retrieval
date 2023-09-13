from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Chat


# Create your views here.
def chatbot(request):
    chats = Chat.objects.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        response = "test"

        chat = Chat(message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})
