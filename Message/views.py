from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse(f"You logged in successfully as {username}")
    else:
        return HttpResponse("failure")

def logout(request):
    if request.user.is_anonymous:
        return HttpResponse("you are not logged in!")
    else:
        username = request.user.username
        auth_logout(request)
        return HttpResponse(f"You logged out from {username}")



def home(request):
    return HttpResponse("<h1>Welcome to Noam Ossia's task</h1>")

@csrf_exempt
@login_required
def createNewMessage(request):
    if request.user.is_anonymous:
        return HttpResponse("you are not logged in!")
    else:
        try:
            receiver = User.objects.filter(username=request.POST['receiver']).get()
            message = request.POST['message']
            subject = request.POST['subject']
            newMessage = Message(sender=request.user.username, receiver=receiver, message=message, subject=subject)
            newMessage.save()
            return HttpResponse("message sent")
        except:
            return HttpResponse("User does not exist")



@api_view(['GET'])
def messageList(request):
    if request.user.is_anonymous:
        return HttpResponse("you are not logged in!")
    else:
        messages = Message.objects.filter(receiver=request.user.username)
        print(request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def readMessage(request):
    if request.user.is_anonymous:
        return HttpResponse("you are not logged in!")
    else:
        message_id = request.POST['message_id']
        try:
            message = Message.objects.filter(id=message_id, receiver=request.user.username).get()
            message.is_read = True
            message.save()
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist:
            return HttpResponse("No matching message!")

@api_view(['GET'])
def messageListUnread(request):
    if request.user.is_anonymous:
        return HttpResponse("you are not logged in!")
    else:
        try:
            messages = Message.objects.filter(receiver=request.user.username, is_read=False)
            print(request.user)
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        except Message.DoesNotExist:
            return HttpResponse("No matching message!")

@csrf_exempt
@login_required
def deleteMessage(request):
    if request.user.is_anonymous:
        return HttpResponse("you are not logged in!")
    else:
        message_id = request.POST['message_id']
        try:
            to_delete = Message.objects.get(id=message_id)
            if (to_delete.sender == request.user.username or to_delete.receiver == request.user.username):
                to_delete.delete()
                return HttpResponse("The message has been deleted successfully")
            else:
                return HttpResponse("Only the sender or receiver can delete this message.")
        except:
            return HttpResponse("No matching message!")

