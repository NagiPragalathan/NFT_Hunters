from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt

from turtle import *


def home(request):
    return render(request,'game_template/index.html')
def browse(request):
    return render(request,'game_template/browse.html')
def details(request):
    return render(request,'game_template/details.html')
def streams(request):
    return render(request,'game_template/streams.html')
def profile(request):
    return render(request,'game_template/profile.html')

# workings
def open_Nft_craft(request):
    hideturtle()
    pensize(10)
    fillcolor('green')
    speed(8)



    right(90)
    begin_fill()
    forward(50)
    for n in [
    (30,200), (90, 200), (30,50)
    ]:
        circle(n[0], 180)
        forward(n[1])
        right(90)
        forward(60)
        end_fill()

        penup()
        goto(0, 100)
        pendown()

        fillcolor('white')
        begin_fill()
    for n in range(2):
        forward(49)
        circle(40, 180)
        end_fill()

        penup()
        goto(-122, 150)
        pendown()

        fillcolor('green')
        begin_fill()
        left(180)
    for i in [20, 150]:
        forward(i)
        circle(10, 90)
        forward(20)
        end_fill()
    done()



# Create your views here.

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')

def getToken(request):
    appId = "6c195af2970e48579689b47d0debf9ca"
    appCertificate = "acb5f43b05c74985aec64f691cf4311c"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)


