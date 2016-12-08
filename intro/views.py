#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from intro.teamname import *
from intro.memberdetail import *

#隊一覧
def top(request):
    t = loader.get_template('top.html')
    c = Context({'teams': teams})
    return HttpResponse(t.render(c))

#️⃣隊員一覧
def index(request, teamId):
    key = int(teamId)
    thisTeam = teams[key-1]
    members = []
    if(key == 1):
        members = kaitentai[:4]
    elif(key == 2):
        members = kaitentai[4:8]
    elif(key == 3):
        members = kaitentai[8:12]
    elif(key == 4):
        members = kaitentai[12:16]
    elif(key == 5):
        members = kaitentai[16:19]
    elif(key == 6):
        members = kaitentai[19:23]
    elif(key == 7):
        members = kaitentai[23:28]
    elif(key == 8):
        members = kaitentai[28:32]
    elif(key == 9):
        members = kaitentai[32:37]
    elif(key == 10):
        members = kaitentai[37:44]
    elif(key == 11):
        members = kaitentai[44:50]
    elif(key == 12):
        members = kaitentai[50:54]
    elif(key == 13):
        members = kaitentai[54:58]
    elif(key == 14):
        members = kaitentai[58:62]
    elif(key == 15):
        members = kaitentai[62:64]
    elif(key == 16):
        members = kaitentai[64:69]
    elif(key == 17):
        members = kaitentai[69:72]
    elif(key == 18):
        members = kaitentai[72:74]
    elif(key == 19):
        members = kaitentai[74:78]
    elif(key == 20):
        members = kaitentai[78:83]
    elif(key == 21):
        members = kaitentai[83:86]
    elif(key == 22):
        members = kaitentai[86:101]
    elif(key == 23):
        members = kaitentai[101:103]
    elif(key == 24):
        members = kaitentai[103:105]

    t = loader.get_template('index.html')
    c = Context({'members': members,
                'name': thisTeam["name"],
                'subtitle': thisTeam["subname"]}
                )
    return HttpResponse(t.render(c))

#️⃣隊員詳細
def detail(request, memberId):
    print memberId
    key = int(memberId)
    teamId = 0
    if(key <= 4):
        teamId = 1
    elif(key <= 8):
        teamId = 2
    elif(key <= 12):
        teamId = 3
    elif(key <= 16):
        teamId = 4
    elif(key <= 19):
        teamId = 5
    elif(key <= 23):
        teamId = 6
    elif(key <= 28):
        teamId = 7
    elif(key <= 32):
        teamId = 8
    elif(key <= 37):
        teamId = 9
    elif(key <= 44):
        teamId = 10
    elif(key <= 50):
        teamId = 11
    elif(key <= 54):
        teamId = 12
    elif(key <= 58):
        teamId = 13
    elif(key <= 62):
        teamId = 14
    elif(key <= 64):
        teamId = 15
    elif(key <= 69):
        teamId = 16
    elif(key <= 72):
        teamId = 17
    elif(key <= 74):
        teamId = 18
    elif(key <= 78):
        teamId = 19
    elif(key <= 83):
        teamId = 20
    elif(key <= 86):
        teamId = 21
    elif(key <= 101):
        teamId = 22
    elif(key <= 103):
        teamId = 23
    elif(key <= 105):
        teamId = 24

    member = kaitentai[key-1]
    print member['name']
    thisTeam = teams[teamId-1]
    t = loader.get_template('detail.html')
    c = Context({'words': member["words"],
                'name' : member["name"],
                'hometown': member["hometown"],
                'career': member["career"],
                'birthday': member["birthday"],
                'deathofage': member["deathofage"],
                'sortie': member["sortie"],
                'teamName': thisTeam["name"],
                'url': thisTeam["url"],
                }
                )
    return HttpResponse(t.render(c))