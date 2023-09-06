from cgi import print_arguments
from django.shortcuts import render, redirect
from ..models import ChatMessage, CustomUser
from ..forms import ChatMessageForm
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chat_view(request):
    user = request.user.customuser
    friends = CustomUser.objects.all()
    context = {"user": user, "friends": friends}
    return render(request, "chat.html", context)

@login_required
def chat_detail(request,pk):
    friend = CustomUser.objects.get(id=pk)
    user = request.user.customuser
    profile = CustomUser.objects.get(id=friend.id)
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user, seen=False)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("chat_detail", pk=friend.id)
    context = {"friend": friend, "form": form, "user":user, 
               "profile":profile, "chats": chats, "num": rec_chats.count()}
    return render(request, "detail.html", context)


def sentMessages(request, pk):
    user = request.user.customuser
    friend = CustomUser.objects.get(id=pk)
    profile = CustomUser.objects.get(id=friend.id)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen=False )
    print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request, pk):
    user = request.user.customuser
    friend = CustomUser.objects.get(id=pk)
    profile = CustomUser.objects.get(id=friend.id)
    arr = []
    chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)


def chatNotification(request):
    user = request.user.customuser
    friends = CustomUser.objects.all()
    arr = []
    for friend in friends:
        chats = ChatMessage.objects.filter(msg_sender__id=friend.id, msg_receiver=user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)
    

# @login_required
# def new_messages(request, pk):
#     last_chat_id = request.GET.get("last_chat_id")
#     friend = CustomUser.objects.get(id=pk)
#     new_messages = ChatMessage.objects.filter(msg_sender=friend, msg_receiver=request.user.customuser, id__gt=last_chat_id)
#     messages = [{"id": message.id, "content": message.content} for message in new_messages]
#     return JsonResponse(messages, safe=False)