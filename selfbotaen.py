# -*- coding: utf-8 -*-
#THAKS TO ALL TEAM BOT

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator

wr = LINE("")
wr.log("Auth Token : " + str(wr.authToken))
wr.log("Timeline Token : " + str(wr.tl.channelAccessToken))

#==============================================================================#
call = wr
oepoll = OEPoll(wr)
wrMID = wr.profile.mid
wrProfile = wr.getProfile()
lineSettings = wr.getSettings()
#==============================================================================#
botStart = time.time()
#==============================================================================#

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

helpMessage ="""╔════════════════════ 
║┈✇✇⫷✯┅ᏇᎥᏒᎴᏁᎥᏋ┅✯⫸✇✇┈
╠════════════════════
╠⍟➣  ᴍʏ ɪᴅ
╠⍟➣  ᴍᴇ
╠⍟➣  ɢɪɴғᴏ
╠⍟➣  ɢᴄʀᴇᴀᴛᴏʀ
╠⍟➣  ɢᴜʀʟ
╠⍟➣  ᴏᴜʀʟ
╠⍟➣  ᴄᴜʀʟ
╠⍟➣  ɢɴᴀᴍᴇ:「ᴛᴇᴋs」
╠⍟➣  ʜᴀɪɪ[ᴛᴀɢ]
╠⍟➣  Kick @
╠⍟➣  ᴄᴇᴋ
╠⍟➣  sɪᴅᴇʀ
╠⍟➣  sɪᴅᴇʀ ᴏɴ
╠⍟➣  sɪᴅᴇʀ ᴏғғ
╠⍟➣  ɢɪғᴛ
╠⍟➣  Hapuschat
╠⍟➣  ɢᴍɪᴅ [Tᴀɢ]
╠⍟➣  ɢᴇᴛ ᴍɪᴅ 「sᴄ」
╠⍟➣  ɢᴇᴛ [ᴛᴀɢ]
╠⍟➣  ᴅᴘ[ᴛᴀɢ]
╠⍟➣  ɪɴғᴏ[ᴛᴀɢ]
╠⍟➣  ʙɪᴏ[ᴛᴀɢ]
╠⍟➣  ᴄᴏᴠᴇʀ[ᴛᴀɢ]
╠⍟➣  ᴄʟᴏɴᴇ [ᴛᴀɢ]
╠⍟➣  ʀᴇᴄʟᴏɴᴇ
╠⍟➣  ɪɴᴠɪᴛᴇ: 「sᴄ」
╠⍟➣  Lɪᴋᴇ ᴏɴ/ᴏғғ
╠⍟➣  Gᴇᴛ ᴘᴏsᴛ ᴏɴ/ᴏғғ
╠⍟➣  ᴍʏ ɢʀᴜᴘ
╠⍟➣  ᴅᴇᴛᴇᴄᴛ ᴛɪᴋᴇʟʟ
╠⍟➣  ᴜɴᴅᴇᴛᴇᴄᴛ ᴛɪᴋᴇʟʟ
╠⍟➣  ᴍʏ ɢʀᴜᴘ
╠⍟➣  sᴀʟᴀᴍ1
╠⍟➣  sᴀʟᴀᴍ2
╠⍟➣  ᴡᴇʟʟᴄᴏᴍᴇ
╠════════════════════
╠⍟➣  ʙᴄᴍᴇᴍʙᴇʀ:「ᴛᴇᴋs」
╠⍟➣  ʙᴄɢʀᴜᴘ:「ᴛᴇᴋs」
╠⍟➣  ʏᴛ: 「ᴛᴇᴋs」
╠⍟➣  ɢʀᴜᴘ ᴘɪᴄᴛ
╠⍟➣  ᴍᴜsɪk 「ᴛᴇᴋs」
╠⍟➣  ᴢᴏᴅɪᴀᴋ:
╠⍟➣  Wɪᴋɪ: 「ᴛᴇᴋs」
╠⍟➣  ᴠɴ: 「ᴛᴇᴋs」
╠⍟➣  ᴠɴ-ᴇɴ: 「ᴛᴇᴋs」
╠⍟➣  ʏᴏᴜᴛᴜʙᴇ: 「ᴛᴇᴋs」
╠⍟➣  /Tᴀɢ [ᴛᴀɢ]
╠⍟➣  /Sᴘᴀᴍ[ᴊᴜᴍʟᴀʜ][ᴛᴇᴋs]
╠⍟➣  /Sᴘᴀᴍᴄᴏɴᴛᴀᴄᴛ
╠⍟➣  /Bʟᴀɴᴋ
╠⍟➣  sᴘ
╠⍟➣  ʀᴜɴᴛɪᴍᴇ
╠⍟➣  ᴋᴀʟᴇɴᴅᴇʀ
╠════════════════════
╠⍟➣  ᴀʟʟ ᴍɪᴍɪᴄ ᴍᴇ[ᴛᴀɢ]
╠⍟➣  ᴜɴᴍɪᴍɪᴄ[ᴛᴀɢ]
╠⍟➣  ᴍɪᴍɪᴄ  /ᴏɴ/ᴏғғ
╠⍟➣  ᴍɪᴍɪᴄ Lɪsᴛ
╠⍟➣  ʙᴀɴɴᴇᴅ[ᴛᴀɢ]
╠⍟➣  ᴜɴʙᴀɴɴᴇᴅ[ᴛᴀɢ]
╠⍟➣  ᴄʟᴇᴀʀ ʙᴀɴ
╠⍟➣  ᴋɪʟʟ ʙᴀɴ
╠⍟➣  ᴀᴅᴅ ʙᴀɴɴᴇᴅ
╠⍟➣  ᴅᴇʟ ʙᴀɴɴᴇᴅ
╠⍟➣  ʙᴀɴ ʟɪsᴛ
╠⍟➣  ᴀᴅᴅ ғʀɪᴇɴᴅ
╠⍟➣  ᴅᴇʟ ғʀɪᴇɴᴅ
╠⍟➣  ғʀɪᴇɴᴅ ʟɪsᴛ
╠⍟➣  ᴍᴇᴍʙᴇʀ Lɪsᴛ
╠════════════════════
╠⍟➣  ʟᴏᴄᴋ ᴊᴏɪɴ「ɪɴ」
╠⍟➣  ᴜɴʟᴏᴄᴋ ᴊᴏɪɴ「ɪɴ」
╠⍟➣  ʟᴏᴄᴋ ᴊᴏɪɴ ɢʀᴜᴘ:「ɢɴ」
╠⍟➣  ᴜɴʟᴏᴄᴋ ᴊᴏɪɴ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠⍟➣  ʟᴏᴄᴋ ǫʀ「ɪɴ」 
╠⍟➣  ᴜɴʟᴏᴄᴋ ǫʀ「ɪɴ」 
╠⍟➣  ʟᴏᴄᴋ ǫʀ ɢʀᴜᴘ:「ɢɴ」
╠⍟➣  ᴜɴʟᴏᴄᴋ ǫʀ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠⍟➣  ʟᴏᴄᴋ ɪɴᴠɪᴛᴇ
╠⍟➣  ᴜɴʟᴏᴄᴋ ɪɴᴠɪᴛᴇ
╠⍟➣  ɪɴᴠɪᴛᴇ ᴏɴ ɢʀᴜᴘ:「ɢɴ」
╠⍟➣  ᴜɴʟᴏᴄᴋ ɪɴᴠɪᴛᴇ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠⍟➣  ᴡᴇʟʟᴄᴏᴍᴇ ᴏɴ/ᴏғғ
╠⍟➣  ʟᴇғᴛ ᴏɴ/ᴏғғ 
╠════════════════════
╠⍟➣  ʀᴇsᴇᴛ ᴀʟʟ sᴇᴛ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠⍟➣  ʟɪsᴛ ᴀᴜᴛᴏᴋɪᴄᴋ
╠⍟➣  ʟɪsᴛ ᴀᴜᴛᴏ ɪɴᴛ
╠⍟➣  ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ
╠⍟➣  ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ ǫʀ
╠⍟➣  ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ
╠⍟➣  ʟɪsᴛ ᴘʀᴏsɪᴅᴇʀ
╠⍟➣  ʟɪsᴛ ᴅᴇᴛᴇᴄᴛ ᴛɪᴋᴇʟʟ
╠════════════════════
╠⍟➣  ʀᴇsᴇᴛ ɢʀᴜᴘ「ɪɴ」 
╠⍟➣  sᴇᴛ「ɪɴ」 
╠⍟➣  sᴛᴀᴛᴜs「ɪɴ」 
╠⍟➣  ᴀᴅᴅ sᴛᴀᴛᴜs「ɪɴ」 
╠⍟➣  ᴀᴅᴅ ᴏғғ「ɪɴ」 
╠⍟➣  Bubar
╠⍟➣  Cancle all
╠════════════════════
╠⍟➣ ᴄᴛᴇᴋs ʟᴇғᴛ:「ᴛᴇᴋs」
╠⍟➣ ʟᴇғᴛ ᴛᴇᴋs
╠⍟➣ ᴄᴛᴇᴋs ᴡᴇʟʟᴄᴏᴍᴇ:「ᴛᴇᴋs」
╠⍟➣ ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴇᴋs
╠⍟➣ ᴄᴛᴇᴋs ᴄᴄᴛᴠ:「ᴛᴇᴋs」
╠⍟➣ ᴄᴄᴛᴠ ᴛᴇᴋs
╠⍟➣ ᴄᴛᴇᴋs ᴀᴅᴅ:「ᴛᴇᴋs」
╠⍟➣ ᴀᴅᴅ ᴛᴇᴋs
╠⍟➣ ᴄᴛᴇᴋs ᴄᴏᴍᴍᴇɴᴛ:「ᴛᴇᴋs」
╠════════════════════
╠⍟➣ ᴄᴛᴇᴋs ᴛᴀɢ1:「ᴛᴇᴋs」
╠⍟➣ ᴛᴀɢ1 ᴄᴇᴋ
╠⍟➣ ᴛᴀɢ1 on
╠⍟➣ ᴛᴀɢ1 off
╠════════════════════
╠⍟➣ ᴄᴛᴇᴋs ᴛᴀɢ2:「ᴛᴇᴋs」
╠⍟➣ ᴄᴛɪᴋᴇʟʟ 2
╠⍟➣ ᴛᴀɢ2 ᴄᴇᴋ
╠⍟➣ ᴛᴀɢ2 on
╠⍟➣ ᴛᴀɢ2 off
╠════════════════════
╠⍟➣ [ɪᴅ/ᴇɴ] ɪɴᴅ ᴛᴏ ᴇɴɢ
╠⍟➣ [ᴇɴ/ɪᴅ] ᴇɴɢ ᴛᴏ ɪᴅ
╠⍟➣ [ɪᴅ/ᴊᴘ] ɪɴᴅ ᴛᴏ ᴊᴘɴ
╠⍟➣ [ᴊᴘ/ɪᴅ] ᴊᴘɴ ᴛᴏ ɪɴᴅ
╠⍟➣ [ɪᴅ/ᴛʜ] ɪɴᴅ ᴛᴏ ᴛʜᴀ
╠⍟➣ [ᴛʜ/ɪᴅ] ᴛʜᴀ ᴛᴏ ɪɴᴅ
╠⍟➣ [ɪᴅ/ᴀʀ] ɪɴᴅ ᴛᴏ ᴀʀʙ
╠⍟➣ [ᴀʀ/ɪᴅ] ᴀʀʙ ᴛᴏ ɪɴᴅ
╠⍟➣ [ɪᴅ/ᴋᴏ] ɪɴᴅ ᴛᴏ ᴋᴏʀ
╠⍟➣ [ᴋᴏ/ɪᴅ] ᴋᴏʀ ᴛᴏ ɪɴᴅ
╠═══════════════════
║ SILENT TΣΔM βΩT
╠═══════════════════
╠⍟➣line://ti/p/~teambotprotect
╠⍟➣line://ti/p/~wira.lord
╚═══════════════════
"""

sid = []
wait = {
    "spamr":False,
    "Invite":True,
    "ainvite":False,
    "atarget":False,
    "dtarget":False,
    "afriend":False,
    "dfriend":False,
    "asilent":False,
    "dsilent":False,
    "santet":True,
    "Autojoin":False,
    "Timeline":False,
    "LikeOn":True,
    "getmid":False,
    "mimic":False,
    }

org = {
    "tmimic":{},
    "Target":{},
    "Silent":{},
    "Friend":{},
    "invitan":{}
    }

pro = {
    'prosider':{},
    'proPoint':{},
    'proTime':{},
    'Protectgr':{},
    'Protectcancl':{},
    'Protectjoin':{},
    'Protectinvite':{},
    'wellcome':False,
    'bymsg':False,
    'intaPoint':{},
    "Autokick":{}
    }

wira = {
    "comment":"╔═════════════════════\nAuto like by:TBP\n╚══════════════════════",
    "cctvteks":"Masuk sayang\nUdah keciduk juga",
    "message":"Cieee kepo @!\n╔═════════════════════\nᵀᴴᴬᴺᴷˢ ᶠᴼᴿ ᴬᴰᴰ ᴹᴱ\n╚══════════════════════",
    "welmsg":"╔═════════════════════\n⫷✯┅ᏇᎥᏒᎴᏁᎥᏋ┅✯⫸\n╚══════════════════════",
    "leftmsg":"╔═════════════════════\n⫷✯┅ᏇᎥᏒᎴᏁᎥᏋ┅✯⫸\n╚══════════════════════",
    "tagteks1":"Tag kk ada apa ya",
    "tagteks2":"iya syang",
    "tagteks3":"kangen ya//-.."
	}

resp = {
    "csticker1":False,
    "csticker2":False,
    "csticker3":False,
    "detectsticker":False,
    "grupsticker":{},
    "Tag1":False,
    "Tag2":False,
    "Tag3":False,
	}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

ciduk = {
    'ceadPoint':{},
    'ceadMember':{},
    'cetTime':{},
    'cOM':{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

myProfile["displayName"] = wrProfile.displayName
myProfile["statusMessage"] = wrProfile.statusMessage
myProfile["pictureStatus"] = wrProfile.pictureStatus

contact = wr.getProfile()
backup = wr.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

#==============================================================================#
def restartBot():
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv) 
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
    
def logError(text):
    wr.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        wr.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
#==============================================================================#
def wiraBot(op):
    try:
        if op.type == 0:
            return
#================[ NOTIFIED_READ_MESSAGE ]================
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = wr.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠ " + Name
                        wait2['ROM'][op.param1][op.param2] = "╠ " + Name
                else:
                    pass
            except:
                pass
        if op.type == 5:
            wr.findAndAddContactsByMid(op.param1)
            if(wira["message"]in[""," ","\n",None]):
                pass
            else:
                wr.sendMessage(op.param1,str(wira["message"]))
#=====================[ CIDUK SIDER ]=======================
        if op.type == 55:
            msg = op.message
            if op.param1 in pro["prosider"]:
                if op.param1 in ciduk['ceadPoint']:
                    x = wr.getContact(op.param2)
                    x_name = x.displayName
                    if x_name not in ciduk['ceadMember'][op.param1]:
                        ciduk['ceadMember'][op.param1] += x_name
                        ciduk['cOM'][op.param1][op.param2] = x_name
                        try:
                            wr.sendMessage(op.param1,""+str(x_name)+"\n"+wira["cctvteks"])
                            wr.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + x.pictureStatus)
                        except:
                            print ("error")
            else:
                pass
#======================[ PROTECT CANCLE ]=================
        if op.type == 32:
            if op.param1 in pro["Protectcancl"]:
                if op.param2 in org["Friend"]:
                    pass
                else:
                    try:
                        wr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        wr.sendMessage(op.param1,"limit")
                        
#=================[ NOTIFIED_INVITE_INTO_GROUP ]==============        
        if op.type == 13:
            if wait["Autojoin"] == True:
                wr.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if op.param2 in org["Silent"]:
                wr.acceptGroupInvitation(op.param1)
#=====================[ PROTECT INVITE ]======================
        if op.type == 12:
            if op.param1 in pro["Protectinvite"]:
                X = wr.getGroup(op.param1)
                orang = [contact.mid for contact in X.invitee]
                for m in orang:
                    org["invitan"][m]=True
                    with open('setting.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
        if op.type == 13:
            if op.param1 in pro["Protectinvite"]:
                if op.param2 in org["Friend"]:
                    if op.param3 in org["Friend"]:
                        pass
                    else:
                        X = wr.getGroup(op.param1)
                        orang = [contact.mid for contact in X.invitee]
                        for m in orang:
                            org["invitan"][m]=True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                else:
                    if op.param3 in org["Friend"]:
                        pass
                    else:
                        try:
                            wr.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            wr.sendMessage(op.param1,"limit")
#=========== [ LEFT MESSAGE ] ==============
        if op.type == 15:
            if pro["bymsg"]==True:
                wrx = wr.getContact(op.param2)
                wr.sendMessage(op.param1,""+ str(wrx.displayName)+"\n"+wira["leftmsg"])
            else:
                pass
#==============[ WELLCOME] ===============
        if op.type == 17:
            if pro["wellcome"] == True:
                if op.param1 in pro["Protectjoin"]:
                    if op.param2 not in org["invitan"]:
                        pass
                    else:
                        ginfo = wr.getGroup(op.param1)
                        wrx = wr.getContact(op.param2)
                        wr.sendMessage(op.param1, "Ehhh  " + str(wrx.displayName) + "\nWellcome to " + str(ginfo.name) +"\n"+ wira["welmsg"])
                        wr.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + ydx.pictureStatus)
                else:
                    ginfo = wr.getGroup(op.param1)
                    wrx = wr.getContact(op.param2)
                    wr.sendMessage(op.param1, "Ehhh  " + str(wrx.displayName) + "\nWellcome to " + str(ginfo.name) +"\n"+ wira["welmsg"])
                    wr.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + wrx.pictureStatus)                    
                    
#==============[ PROTECT JOIN ]==============
        if op.type == 17:
            if op.param1 in pro["Protectjoin"]:
                if op.param2 in org["Friend"]:
                    pass
                elif op.param2 in org["invitan"]:
                    del org["invitan"][op.param2]
                    pass
                else:
                    try:
                        wr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        wr.sendMessage(op.param1,"limit")
#=========== [ GHOST MODE ] =============
#===========[ PROTECT QR friend ]==========           
        if op.type == 11:
           if op.param1 in pro["Protectgr"]:
              if op.param2 in org["Friend"]:
                pass
              else:
                try:
                  X = wr.getGroup(op.param1)
                  X.preventedJoinByTicket = True
                  wr.updateGroup(X)
                  Ti = wr.reissueGroupTicket(op.param1)
                  wr.acceptGroupInvitationByTicket(op.param1,Ti)
                  wr.sendMessage(op.param1,wr.getContact(op.param2).displayName + "ᴊᴀɴɢᴀɴ ᴍᴀɪɴᴀɴ ᴋᴏᴅᴇ Qʀ ɢᴏʙʟᴏᴋ")
                  wr.kickoutFromGroup(op.param1,[op.param2])
                  wr.updateGroup(X)
                  wr.leaveRoom(op.param1)
                except:
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventedJoinByTicket = True
                  yd.updateGroup(Z)
                  Ti = wr.reissueGroupTicket(op.param1)
                  wr.acceptGroupInvitationByTicket(op.param1,Ti)
                  wr.sendText(op.param1,wr.getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                  wr.kickoutFromGroup(op.param1,[op.param2])
                  wr.updateGroup(X)
                  wr.leaveRoom(op.param1)
                 
#=============== [ NOTIFIED_KICKOUT_FROM_GROUP ]===========
        if op.type == 19:
            if op.param1 in pro["Autokick"]:
                if op.param2 in org["Friend"]:
                    pass
                else:
                    try:
                        wr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        wr.sendMessage(op.param1,"limit")
                   
						
            if op.param3 in org["Friend"]:
                if op.param2 in org["Friend"]:
                    pass
                else:                   
                    try:
                        wr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        wr.sendMessage(op.param1,"limit")
                    try:
                    	wr.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            G = wr.getGroup(op.param1)
                            G.preventJoinByTicket = False
                            wr.updateGroup(G)
                            invsend = 0
                            Ticket = wr.reissueGroupTicket(op.param1)
                            wr.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G = wr.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            wr.updateGroup(G)
                        except Exception as e:
                            print(e)

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
                if msg.contentType == 7:
                    if resp["csticker1"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID1: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        wr.sendMessage(msg.to, tikell)

                    elif resp["csticker2"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID2: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        wr.sendMessage(msg.to, tikell)

                    elif resp["csticker3"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID3: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        wr.sendMessage(msg.to, tikell)
                    else:
                        pass
                        
                if msg.contentType == 13:
                    if wait["atarget"]==True:
                        if msg.contentMetadata["mid"] in org["Target"]:
                            wr.sendMessage(msg.to, "was save")
                            wait["atarget"]=False
                        else:
                            org["Target"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to, "save succes")
                            wait["atarget"]=False

                    elif wait["dtarget"]==True:
                        if msg.contentMetadata["mid"] in org["Target"]:
                            del org["Target"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wait["dtarget"]=False
                            wr.sendMessage(msg.to,"Target deleted")
                        else:
                            wr.sendMessage(msg.to,"Target not found")
#=====================[ MODE SILENT ]=================--======
                if msg.contentType == 13:
                    if wait["asilent"]==True:
                        if msg.contentMetadata["mid"] in org["Silent"]:
                            wr.sendMessage(msg.to, "siap on bos")
                            wait["asilent"]=False
                        else:
                            org["Silent"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to, "TBP succes")
                            wait["asilent"]=False

                    elif wait["dsilent"]==True:
                        if msg.contentMetadata["mid"] in org["Silent"]:
                            del org["Silent"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"Silent deleted")
                            wait["dsilent"]=False
                        else:
                            wr.sendMessage(msg.to,"Silent not found")
                            wait["dsilent"]=False
                    else:
                        pass
#=====================[ SEPAM ]========================
                if msg.contentType == 13:
                    if wait["getmid"]==True:
                        x = msg.contentMetadata["mid"]
                        wr.sendMessage(msg.to,x)
                        wait["getmid"]=False

                if msg.contentType == 13:
                    if wait["santet"]==True:
                        x = msg.contentMetadata["mid"]
                        wr.findAndAddContactsByMid(x)
                        try:
                            M = Message()
                            M.to = x
                            M.contentType = 13
                            M.contentMetadata = {'mid': "'"}
                            wr.sendMessage(M)
                            wr.sendMessage(M)
                            wait["santet"]=False
                        except:
                            pass
#========================[ INVITE ]===================
                if msg.contentType == 13:
                    if wait["afriend"]==True:
                        if msg.contentMetadata["mid"] in org["Friend"]:
                            wr.sendMessage(msg.to, "Team done")
                            wait["afriend"]=False
                        else:
                            org["Friend"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to, "Tem succes")
                            wait["afriend"]=False

                    elif wait["dfriend"]==True:
                        if msg.contentMetadata["mid"] in org["Friend"]:
                            del org["Friend"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"Hapus teman")
                            wait["dfriend"]=False
                        else:
                            wr.sendMessage(msg.to,"Teman tidak di temukan")
                            wait["dfriend"]=False

#=====================[ MODE INVITE ]==================
                if msg.contentType == 13:
                    if wait["Invite"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = wr.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                wr.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invite"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                wr.findAndAddContactsByMid(target)
                                wr.inviteIntoGroup(msg.to,[target])
                                wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴍᴇɴɢɪɴᴠɪᴛᴇ ᴊᴏᴍʙʟᴏ ɪɴɪ \n➡" + _name)
                                wait["Invite"] = False
                                break
                else:
                    pass
#==================[ RECEIVE_MESSAGE ]===============
        if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.text in ["Help"]:
                    wr.sendMessage(msg.to,helpMessage)          
					
        if op.type == 25:
            msg = op.message
            if msg.text is None:
                return
            if msg.text in ["My id"]:
                if msg.toType == 2:
                    wr.sendMessage(msg.to,wrMID)
                    
            elif msg.text in ["Me"]:
            	wr.sendMessage(receiver, None, contentMetadata={'mid': wrMID}, contentType=13)
            
            elif msg.text in ["Ginfo"]:
                if msg.toType == 2:
                    ginfo = wr.getGroup(msg.to)
                    gCreator = ginfo.creator.displayName
                    if gCreator is None:
                        gCreator = "Error"
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventedJoinByTicket == True:
                        u = "close"
                    else:
                        u = "open"
                    try:
                        wr.sendMessage(msg.to,"╔══════════════\n╠═༼≝₷₭ ɢʀᴜᴘ ɴᴀᴍᴇ ≝₷₭༽\n╠ ➽ " + str(ginfo.name) + "\n╠══════════════\n╠═ ༼≝₷₭  ɢʀᴜᴘ ᴄʀᴇᴀᴛᴏʀ ⟧≝₷₭༽\n╠ ➽ " + gCreator + "\n╠══════════════\n╠ ➽ ᴍᴇᴍʙᴇʀs: " + str(len(ginfo.members)) + " ᴍᴇᴍʙᴇʀs\n╠ ➽ ᴘᴇɴᴅɪɴɢ: " + sinvitee + " ᴘᴇᴏᴘʟᴇ\n╠ ➽ ᴜʀʟ : " + u + "\n╚══════════════")
                        wr.sendMessage(msg.to,"「ɢɪᴅ:」 \n➽ " + msg.to)
                        wr.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                    except:
                        wr.sendMessage(msg.to,"╔══════════════\n╠═༼≝₷₭  ɢʀᴜᴘ ɴᴀᴍᴇ ≝₷₭༽\n╠ ➽ " + str(ginfo.name) + "\n╠══════════════\n╠═༼≝₷₭  ɢʀᴜᴘ ᴄʀᴇᴀᴛᴏʀ ≝₷₭༽\n╠ ➽ " + gCreator + "\n╚══════════════")
                        wr.sendMessage(msg.to,"「ɢɪᴅ:」 \n➽ " + msg.to)
                        wr.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                        
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                group = wr.getGroup(msg.to)
                GS = group.creator.mid
                wr.sendContact(msg.to,GS)            
                wr.sendMessage(msg.to,"Sijones ini ɴᴏʜ ʏɢ ʙɪᴋɪɴ ɢʀᴜᴘ....")
                
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = wr.getGroup(msg.to)
                    if x.preventedJoinByTicket == True:
                        wr.sendMessage(msg.to,"ǫʀ ɴʏᴀ ᴅɪ ᴀɴᴜ ᴅᴜʟᴜ ʙᴏss..")
                    elif x.preventedJoinByTicket == False:
                        wr.updateGroup(x)
                        gurl = wr.reissueGroupTicket(msg.to)
                        wr.sendMessage(msg.to,"http://line.me/R/ti/g/" + gurl)
                    else:
                        pass
                        
            elif msg.text in ["Ourl"]:
              if msg.toType == 2:
                X = wr.getGroup(msg.to)
                if X.preventedJoinByTicket == False:
                    wr.sendMessage(msg.to,"⟦Qʀ ᴡᴀs ᴏᴘᴇɴ⟧")
                else:
                    X.preventedJoinByTicket = False
                    wr.updateGroup(X)
                    wr.sendMessage(msg.to,"⟦Qʀ ᴏᴘᴇɴ⟧")
                    
            elif msg.text in ["Curl"]:
              if msg.toType == 2:
                X = wr.getGroup(msg.to)
                if X.preventedJoinByTicket == True:
                    wr.sendMessage(msg.to,"⟦Qʀ ᴡᴀs ᴄʟᴏsᴇ⟧")
                else:
                    X.preventedJoinByTicket = True
                    wr.updateGroup(X)
                    wr.sendMessage(msg.to,"⟦Qʀ ᴄʟᴏsᴇ⟧")
                    
            elif "Gname: " in msg.text:
                if msg.toType == 2:
                    X = wr.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    wr.updateGroup(X)
                    wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴛᴏ:\n\n"+X.name)
                    
            elif msg.text in ["Reject"]:
              if msg.toType == 2:
                gid = wr.getGroupIdsInvited()
                for i in gid:
                    wr.rejectGroupInvitation(i)
                wr.sendMessage(msg.to,"done reject")

            elif "Bcmember: " in msg.text:
                xres = msg.text.replace("Bcmember: ","")
                group = wr.getGroup(msg.to)
                mem = [contact.mid for contact in group.members]
                cmem = wr.getContacts(mem)
                nc = ""
                for x in range(len(cmem)):
                    try:
                        wr.sendMessage(cmem[x].mid,xres)
                        nc += "\n" + cmem[x].displayName
                    except:
                        pass
                wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʙᴄ ᴛᴏ :\n%s\n\nᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs: %s"%(nc,str(len(cmem))))
            #    print "done bc"
            elif "Bcgrup: " in msg.text:
                bc = msg.text.replace("Bcgrup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                    wr.sendMessage(i,bc+"\n\nSILENT TΣΔM βΩT")
                wr.sendMessage(msg.to,"⟦ʙʀᴏᴀᴅᴄᴀsᴛ sᴜᴄᴄᴇs⟧")
            elif "Lirik: " in msg.text:
                try:
                    songname = msg.text.replace('Lirik: ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        wr.sendMessage(msg.to, hasil)
                except Exception as wak:
                        wr.sendMessage(msg.to, str(wak))
            elif "Image: " in msg.text:
                try:
                    query = msg.text.replace("Image:", "")
                    images = wr.image_search(query)
                    wr.sendImageWithURL(receiver, images)
                except Exception as e:
                    wr.sendMessage(receiver, str(e))
            elif "Yt: " in msg.text:
                query = msg.text.replace("Yt: ","")
                with requests.session() as s:
                    s.headers['user-agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    wr.sendMessage(msg.to,hasil)
            elif msg.text in ["mid"]:
                wait["getmid"]=True
                wr.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif "Gmid @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            wr.sendMessage(msg.to,str(mention['M']))
                        except Exception as e:
                            pass
            elif "Get @" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = wr.getContact(key1)
                vcx = mmid.mid
                wr.sendContact(msg.to,vcx)
            elif "dp @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = wr.getContact(mention['M'])
                            wr.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                        except Exception as e:
                            pass
            elif "info @" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = wr.getContact(key1)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    wr.sendMessage(msg.to,"Nama:\n" + contact.displayName)
                    wr.sendMessage(msg.to,"Bio:\n" + contact.statusMessage)
                    wr.sendImageWithURL(msg.to,image)
                except:
                    pass
            elif "bio @" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = yd.getContact(key1)
                try:
                    wr.sendMessage(msg.to,contact.statusMessage)
                except:
                    wr.sendMessage(msg.to,"⟦ʙɪᴏ ᴇᴍᴘᴛʏ⟧")

            elif "Grup pict" in msg.text:
                    group = wr.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    wr.sendImageWithURL(msg.to,path)
                    
            elif "Kedipin: " in msg.text:
                txt = msg.text.replace("Kedipin: ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                wr.sendMessage(msg.to, t1 + txt + t2)
                
            elif "Insta: " in msg.text:
                try:
                    instagram = msg.text.lower().replace("Insta: ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    wr.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                    wr.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	wr.sendMessage(msg.to, str(njer))

            elif "Zodiak: " in msg.text:
                tanggal = msg.text.replace("Zodiak: ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                wr.sendMessage(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
            elif "Wiki: " in msg.text:
                try:
                    wiki = msg.text.lower().replace("Wiki: ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=1)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    wr.sendMessage(msg.to, pesan)
                except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            wr.sendMessage(msg.to, pesan)
                        except Exception as e:
                            wr.sendMessage(msg.to, str(e))

#==================[ REBOOT ]===================
            elif msg.text in ["Reboot"]:
                    try:
                        wr.sendMessage(msg.to,"ʀᴇsᴛᴀrᴛɪɴɢ .....")
                        restartBot()
                    except:
                        wr.sendMessage(msg.to,"Please wait")
                        restartBot()
                        pass
                        
            elif msg.text in ["Sp"]:
                start = time.time()
                wr.sendMessage(msg.to, "ѕaвar вoѕѕ..")
                elapsed_time = time.time() - start
                wr.sendMessage(msg.to, "%ss" % (elapsed_time))
                
            elif msg.text in ["Refresh"]:
                    wr.sendMessage(msg.to, "Bot has been restarted")
                    restart_program()
                    
            elif msg.text in ["Time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                wr.sendMessage(msg.to, rst)
                
            elif msg.text in ["Runtime"]:
                timeNow = time.time()
                runtime = timeNow - botStart
                runtime = format_timespan(runtime)
                wr.sendMessage(msg.to, "ʙᴏᴛ ʀᴜɴ  {}".format(str(runtime)))
                
            elif msg.text in ["Tanggal"]:
                    tz = pytz.timezone("Asia/Hong_Kong")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    wr.sendMessage(msg.to, readTime)  

            elif "/spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[1])
                teks = msg.text.replace("/spam "+str(jmlh),"")
                for i in range(jmlh):
                    if str(txt[2])==None:
                        wr.sendMessage(msg.to, "typo tu bos")
                    else:
                        try:
                            wr.sendMessage(msg.to, teks)
                        except:
                            wr.sendMessage(msg.to, "cek lagi deh bos")
                            
            elif "/tag @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            coii = wr.getContact(mention['M'])
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)
                            wr.tag(msg.to,coii.mid)                            
                        except:
                            print ("error")
                        print ("spamtag Berhasil.")
                        
            elif msg.text in ["/blank"]:
                blank = "'"
                wr.sendContact(msg.to, blank)	

#=================================================
            elif msg.text in ["bubar"]:
                if msg.toType == 2:
                    group = wr.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    for x in nama:
                            if x not in org["Friend"]:
                                try:
                                    wr.kickoutFromGroup(msg.to,[x])
                                except:
                                    print ("imit")
#==================[ CLONE MODE ]====================
            elif "santet grup: " in msg.text:
                ng = msg.text.replace("santet grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            grup = wr.getGroup(i)
                            M.to = grup.id
                            M.contentType = 13
                            M.contentMetadata = {'mid': "ub1c5a71f27b863896e9d44bea857d35b"}
                wr.sendMessage(M)
                wr.sendMessage(msg.to,"「sᴀɴntᴇᴛ ᴛᴇʀᴋɪʀɪᴍ ʙᴏss」")
            elif msg.text in ["Santet"]:
                wait["santet"]=True
                wr.sendMessage(msg.to,"target")
#=================================================
            elif "Clone @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = yd.getProfile()
                            backup.displayName = profile.displayName
                            backup.statusMessage = profile.statusMessage
                            backup.pictureStatus = profile.pictureStatus
                            wr.cloneContactProfile(mention['M'])
                            wr.sendMessage(msg.to,"ᴄʟᴏɴᴇ sᴜᴄᴄᴇs ..")
                        except Exception as error:
                            print (error)
#=================================================
            elif msg.text in ["Reclone"]:
                try:
                    wrProfile.displayName = str(myProfile["displayName"])
                    wrProfile.statusMessage = str(myProfile["statusMessage"])
                    wrProfile.pictureStatus = str(myProfile["pictureStatus"])
                    wr.updateProfileAttribute(8, ydProfile.pictureStatus)
                    wr.updateProfile(ydProfile)
                    wr.sendMessage(msg.to,"reᴄʟᴏɴᴇ sᴜᴄᴄᴇs ..")
                except Exception as e:
                    wr.sendMessage(msg.to, str (e))
#=================================================
            elif "Kick @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            wr.kickoutFromGroup(msg.to, [mention['M']])							
                        except:
                            wr.sendMessage(msg.to, "ʟɪᴍɪᴛ ʙᴏss..")
#=================================================
            elif msg.text in ["Salam"]:
                wr.sendMessage(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
            elif msg.text in ["Salam2"]:
                wr.sendMessage(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
#=================================================
            elif "Reset tikell grup: " in msg.text:
                ng = msg.text.replace("Reset tikell grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            del resp["grupsticker"][i]
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
#=================================================
            elif msg.text in ["All protect on"]:
                    pro["Protectgr"][msg.to] = True
                    pro["Protectjoin"][msg.to] = True
                    pro["Protectcancl"][msg.to] = True
                    pro["Protectinvite"][msg.to] = True
                    pro["Autokick"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    wr.sendMessage(msg.to,"ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏɴ")
            elif msg.text in ["All protect off"]:
                if msg.to in pro["Protectgr"]:
                    try:
                        del pro["Protectgr"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectcancl"]:
                    try:
                        del pro["Protectcancl"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectinvite"]:
                    try:
                        del pro["Protectinvite"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectjoin"]:
                    try:
                        del pro["Protectjoin"][msg.to]
                    except:
                        pass
                if msg.to in pro["Autokick"]:
                    try:
                        del pro["Autokick"][msg.to]
                    except:
                        pass
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏғғ")
            elif "All protect on grup: " in msg.text:
                ng = msg.text.replace("All protect on grup: ","")
                gid = yd.getGroupIdsJoined()
                for i in gid:
                        h = yd.getGroup(i).name
                        if h == ng:
                            pro["Protectgr"][i]=True
                            pro["Protectjoin"][msg.to] = True
                            pro["Protectcancl"][msg.to] = True
                            pro["Protectinvite"][msg.to] = True
                            pro["Autokick"][msg.to] = True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏɴ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "All protect off grup: " in msg.text:
                ng = msg.text.replace("All protect off grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            if i in pro["Protectgr"]:
                                try:
                                    del pro["Protectgr"][i]
                                except:
                                    pass
                            if i in pro["Protectcancl"]:
                                try:
                                    del pro["Protectcancl"][i]
                                except:
                                    pass
                            if i in pro["Protectinvite"]:
                                try:
                                    del pro["Protectinvite"][i]
                                except:
                                    pass
                            if i in pro["Protectjoin"]:
                                try:
                                    del pro["Protectjoin"][i]
                                except:
                                    pass
                            if i in pro["Autokick"]:
                                try:
                                    del pro["Autokick"][i]
                                except:
                                    pass
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
#=================================================
            elif msg.text in ["Lock invite"]:
                pro["Protectinvite"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ɪɴᴠɪᴛᴇ ᴏɴ ᴘʀᴏᴛᴇᴄᴛ")
            elif msg.text in ["Unlock invite"]:
                del pro["Protectinvite"][msg.to]
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ɪɴᴠɪᴛᴇ ᴜɴᴘʀᴏᴛᴇᴄᴛ")
            elif "Unlock invite grup: " in msg.text:
                ng = msg.text.replace("Unlock invite grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            del pro["Protectinvite"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock invite grup: " in msg.text:
                ng = msg.text.replace("Lock invite grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            pro["Protectinvite"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all invite"]:
                pro["Protectinvite"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================
            elif msg.text in ["Lock cancel"]:
                pro["Protectcancl"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴏɴ ᴘʀᴏᴛᴇᴄᴛ")
            elif msg.text in ["Unlock cancel"]:
                del pro["Protectcancl"][msg.to]
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴜɴᴘʀᴏᴛᴇᴄᴛ")
            elif "Unlock cancel grup: " in msg.text:
                ng = msg.text.replace("Unlock cancel grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            del pro["Protectcancl"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock cancel grup: " in msg.text:
                ng = msg.text.replace("Lock cancel grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            pro["Protectcancl"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all cancel"]:
                pro["Protectcancl"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================                
            elif text.lower().startswith("musik"):
                            try:
                                search = text.lower().replace("musik ","")
                                params = {"search": search}
                                r = requests.get("https://farzain.xyz/api/premium/joox.php?apikey=al11241519&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))                    
                                wr.sendImageWithURL(msg.to, str(data["gambar"]))
                                wr.sendMessage(msg.to, str(hasil))
                                wr.sendMessage(msg.to, "Sabar boaku")
                                wr.sendAudioWithURL(msg.to, str(audio["mp3"]))                    
                                wr.sendMessage(msg.to, str(data["lirik"]))
                            except Exception as error:
                            	pass                         
#=================================================
            elif msg.text in ["Lock join"]:
                pro["Protectjoin"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴊᴏɪɴ ᴏɴ ᴘʀᴏᴛᴇᴄᴛ")
            elif msg.text in ["Unlock join"]:
                del pro["Protectjoin"][msg.to]
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴊᴏɪɴ ᴜɴᴘʀᴏᴛᴇᴄᴛ")
            elif "Unlock join grup: " in msg.text:
                ng = msg.text.replace("Unlock join grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            del pro["Protectjoin"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock join grup: " in msg.text:
                ng = msg.text.replace("Lock join grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            pro["Protectjoin"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all join"]:
                pro["Protectjoin"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================
            elif msg.text in ["Left on"]:
                pro["bymsg"]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to, "ᴏᴜᴛ ᴍᴇssᴀɢᴇ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Left off"]:
                pro["bymsg"]=False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to, "ᴏᴜᴛ ᴍᴇssᴀɢᴇ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=================================================
            elif msg.text in ["Welcome on"]:
                pro["wellcome"]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to, "ᴡᴇʟʟᴄᴏᴍᴇ ᴍsɢ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Welcome off"]:
                pro["wellcome"]= False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to, "ᴡᴇʟʟᴄᴏᴍᴇ ᴍsɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=================================================
            elif msg.text in ["Autokick on"]:
                pro["Autokick"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Autokick off"]:
                pro["Autokick"][msg.to]=False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴋɪᴄᴋ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
            elif "Unlock autokick grup: " in msg.text:
                ng = msg.text.replace("Unlock autokick grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            del pro["Autokick"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock autokick grup: " in msg.text:
                ng = msg.text.replace("Lock autokick grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            pro["Autokick"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all autokick"]:
                pro["Autokick"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================                
            elif "Sider on grup: " in msg.text:
                ng = msg.text.replace("Sider on grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                  h = wr.getGroup(i).name
                  if h == ng:
                    wr.sendMessage(i,"ɢᴇᴛ ɢʀᴏᴜᴘ ᴅᴏɴᴇ")
                    wr.sendMessage(i,"ɢᴇᴛ ᴍᴇᴍʙᴇʀ ᴅᴏɴᴇ")
                    wr.sendMessage(i,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏɴ")
                    wr.sendMessage(i,"ᴀᴜᴛᴏ sɪᴅᴇʀ ʙʏ: wira")
                    pro["prosider"][i] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    try:
                        del ciduk['ceadPoint'][i]
                        del ciduk['ceadMember'][i]
                    except:
                        pass
                    now2 = datetime.now()
                    ciduk['ceadPoint'][i] = msg.id
                    ciduk['ceadMember'][i] = ""
                    ciduk['cetTime'][i] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    ciduk['cOM'][i] = {}
                    wr.sendMessage(msg.to,"sider on that grup")

            elif "Sider off grup: " in msg.text:
                ng = msg.text.replace("Sider off grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                  h = wr.getGroup(i).name
                  if h == ng:
                        wr.sendMessage(i,"ᴄʟᴇᴀʀ ᴍᴇᴍʙᴇʀ ᴅᴏɴᴇ")
                        wr.sendMessage(i,"sɪᴅᴇʀ sᴇᴛ ᴏғғ")
                        wr.sendMessage(i,"ᴀᴜᴛᴏ sɪᴅᴇʀ ʙʏ: wira")
                        del pro["prosider"][i]
                        with open('pro.json', 'w') as fp:
                            json.dump(pro, fp, sort_keys=True, indent=4)
                        try:
                            del ciduk['ceadPoint'][i]
                            del ciduk['ceadMember'][i]
                            wr.sendMessage(msg.to,"sider off")
                        except:
                            pass
#=============================================
            elif "Reset all set grup: " in msg.text:
                ng = msg.text.replace("Reset all set grup: ","")
                gid = wr.getGroupIdsJoined()
                for i in gid:
                        h = wr.getGroup(i).name
                        if h == ng:
                            del pro["Protectgr"][i]
                            del pro["Protectcancl"][i]
                            del pro["Protectinvite"][i]
                            del pro["Protectjoin"][i]
                            del pro["Autokick"][i]
                            del pro["intaPoint"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ᴀʟʟ sᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
#=============================================
            elif msg.text in ["Tag1 on"]:
                    resp["Tag1"]=True
                    resp["Tag2"]=True
                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    wr.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Tag1 off"]:
                    resp["Tag1"]=False
                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    wr.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=============================================
            elif msg.text in ["Tag2 on"]:
                    resp["Tag1"]=True
                    resp["Tag2"]=True

                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    wr.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Tag2 off"]:
                    resp["Tag2"]=False
                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    wr.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=============================================
            elif msg.text in ["Reset"]:
                if msg.to in pro["Protectgr"]:
                    try:
                        del pro["Protectgr"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectcancl"]:
                    try:
                        del pro["Protectcancl"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectinvite"]:
                    try:
                        del pro["Protectinvite"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectjoin"]:
                    try:
                        del pro["Protectjoin"][msg.to]
                    except:
                        pass
                if msg.to in pro["Autokick"]:
                    try:
                        del pro["Autokick"][msg.to]
                    except:
                        pass
                if msg.to in pro["intaPoint"]:
                    try:
                        del pro['intaPoint'][msg.to]
                    except:
                        pass
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴀʟʟ sᴇᴛ ᴄʟᴇᴀʀ")
            elif msg.text in ["Set"]:
                md = "╔════════════════════\n╠➣SILENT TΣΔM βΩT\n╠════════════════════\n"
                if msg.to in pro["intaPoint"]: md+="╠➣ᴀᴜᴛᴏ ɪɴ : ✔\n"
                else: md +="╠➣ᴀᴜᴛᴏ ɪɴ : ❌\n"
				
                if msg.to in pro["Protectgr"]: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ɢʀᴜᴘ : ✔\n"
                else: md +="╠➣ᴘʀᴏᴛᴇᴄᴛ ɢʀᴜᴘ : ❌\n"
				
                if msg.to in pro["Protectcancl"]: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ : ✔\n"
                else: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ : ❌\n"
				
                if msg.to in pro["Protectjoin"]: md+="╠➣ᴘʀᴛᴏᴛᴇᴄᴛ ᴊᴏɪɴ : ✔\n"
                else: md+= "╠➣ᴘʀᴛᴏᴛᴇᴄᴛ ᴊᴏɪɴ : ❌\n"
				
                if msg.to in pro["Protectinvite"]: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠ : ✔\n"
                else: md+= "╠➣ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠ : ❌\n"
				
                if msg.to in pro["Autokick"]: md+="╠➣ᴀᴜᴛᴏ ᴋɪᴄᴋ : ✔\n╠════════════════════\n╠➣line://ti/p/~dhenz415\n╠➣line://ti/p/~tambotprotect\n╚════════════════════"
                else:md+="╠➣ᴀᴜᴛᴏ ᴋɪᴄᴋ : ❌\n╠════════════════════\n╠➣line://ti/p/~dhenz415\n╠➣line://ti/p/~teambotprotect\n╚════════════════════"
				
                wr.sendMessage(msg.to,md)
            elif msg.text in ["Add off"]:
                wait["Invi"]=False
                wait["ainvite"]=False
                wait["atarget"]=False
                wait["dtarget"]=False
                wait["afriend"]=False
                wait["dfriend"]=False
                wait["asilent"]=False
                wait["dsilent"]=False
                wait["gsilrnt"]=False
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴀʟʟ ᴀᴅᴅ ᴄʟᴇᴀʀ")
            elif msg.text in ["Add status"]:
                md = "╔════════════════════\n╠SILENT TΣΔM βΩT\n╠════════════════════\n"
                if wait["Invi"] == True: md+="╠➣Invite : ✔\n"
                else:md+="╠➣Invite : ❌\n"
                if wait["atarget"] == True: md+="╠➣ᴀᴅᴅ ʙᴀɴɴᴇᴅ : ✔\n"
                else:md+="╠➣ᴀᴅᴅ ʙᴀɴɴᴇᴅ : ❌\n"
                if wait["dtarget"] == True: md+="╠➣ᴅᴇʟ ʙᴀɴɴᴇᴅ : ✔\n"
                else:md+="╠➣ ᴅᴇʟ ʙᴀɴɴᴇᴅ : ❌\n"
                if wait["atebz"] == True: md+="╠➣ᴀᴅᴅ sillent : ✔\n"
                else:md+="╠➣ ᴀᴅᴅ sillent : ❌\n"
                if wait["dtebz"] == True: md+="╠➣ᴅᴇʟ sillent : ✔\n"
                else:md+="╠➣ᴅᴇʟ sillent : ❌\n"
                if wait["afriend"] == True: md+="╠➣ᴀᴅᴅ ғʀɪᴇɴᴅ : ✔\n"
                else:md+="╠➣add friend : ❌\n"
                if wait["dfriend"] == True: md+="╠➣ᴅᴇʟ ғʀɪᴇɴᴅ : ✔\n"
                else:md+="╠➣ᴅᴇʟ ғʀɪᴇɴᴅ : ❌\n"
                if wait["getmid"] == True: md+="╠➣ɢᴇᴛ ᴍɪᴅ : ✔\n╠════════════════════\n╠➣line://ti/p/~teambotprotect\n╠➣line://ti/p/~dhenz415\n╚════════════════════"
                else:md+="╠➣ɢᴇᴛ ᴍɪᴅ : ❌\n╠════════════════════\n╠➣line://ti/p/~dhenz415\n╠➣line://ti/p/~teambotprotect\n╚════════════════════"
                wr.sendMessage(msg.to,md)
            elif msg.text in ["Status"]:
                md = "╔════════════════════\n╠SILENT TΣΔM βΩT\n╠════════════════════\n"
                if wait["Autojoin"] == True: md+="╠➣ᴀᴜᴛᴏᴊᴏɪɴ : ✔\n"
                else:md+="╠➣ᴀᴜᴛᴏᴊᴏɪɴ : ❌\n"
                if resp["Tag1"] == True: md+="╠➣ ᴍᴇɴᴛɪᴏɴ1 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ1 : ❌\n"
                if resp["Tag2"] == True: md+="╠➣ᴍᴇɴᴛɪᴏɴ2 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ2 : ❌\n"
                if resp["Tag3"] == True: md+="╠➣ᴍᴇɴᴛɪᴏɴ3 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ3 : ❌\n"
                if wait["Invite"] == True: md+="╠➣ɪɴᴠɪᴛᴇ : ✔\n"
                else:md+="╠➣ɪɴᴠɪᴛᴇ : ❌\n"
                if wait["LikeOn"] == True: md+="╠➣ᴀᴜᴛᴏʟɪᴋᴇ : ✔\n"
                else:md+="╠➣ᴀᴜᴛᴏʟɪᴋᴇ : ❌\n"
                if wait["getmid"] == True: md+="╠➣ɢᴇᴛ ᴍɪᴅ : ✔\n"
                else:md+="╠➣ɢᴇᴛ ᴍɪᴅ : ❌\n"
                if wait["Timeline"] == True: md+="╠➣ɢᴇᴛ ᴘᴏsᴛ : ✔\n"
                else:md+="╠➣ɢᴇᴛ ᴘᴏsᴛ : ❌\n"
                if pro["wellcome"] == True: md+="╠➣ᴡeʟʟᴄᴏᴍᴇ ᴛᴇᴋs : ✔\n"
                else:md+="╠➣ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴇᴋs : ❌\n"
                if pro["bymsg"] == True: md+="╠➣ʙʏᴇ ᴍsɢ ᴛᴇᴋs : ✔\n╠════════════════════\n╠➣line://ti/p/~tambotprotect\n╠➣line://ti/p/~dhenz415\n╚════════════════════"
                else:md+="╠➣ʙʏᴇ ᴍsɢ ᴛᴇᴋs : ❌\n╠════════════════════\n╠➣line://ti/p/~tambotprotect\n╠➣line://ti/p/~tambotprotect\n╚════════════════════"
                wr.sendMessage(msg.to,md)
#=============================================
            elif msg.text in ["Cek ginfo"]:
                if msg.toType == 2:
                    ginfo = yd.getGroup(msg.to)
                    gCreator = ginfo.creator.displayName
                    if gCreator is None:
                        gCreator = "Error"
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventedJoinByTicket == True:
                        u = "close"
                    else:
                        u = "open"
                    try:
                        wr.sendMessage(msg.to,"「ɢʀᴜᴘ ɴᴀᴍᴇ」 \n➽ " + ginfo.name)
                        time.sleep(0.2)
                        wr.sendMessage(msg.to,"「ɢʀᴜᴘ ᴄʀᴇᴀᴛᴏʀ」 \n➽ "+ gCreator )
                        time.sleep(0.2)
                        wr.sendMessage(msg.to,"「ᴍᴇᴍʙᴇʀs」 \n➽" + str(len(ginfo.members)) + " ᴍᴇᴍʙᴇʀs")
                        time.sleep(0.2)
                        wr.sendMessage(msg.to,"「ᴘᴇɴᴅɪɴɢ:」 " + sinvitee + " ᴘᴇᴏᴘʟᴇ")
                        time.sleep(0.2)
                        wr.sendMessage(msg.to,"「ᴜʀʟ:」 \n➽ " + u )
                        wr.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                    except:
                        wr.sendMessage(msg.to,"get info failed")
            elif msg.text in ["Silent cek grup set"]:
                if msg.to in pro["intaPoint"]:
                    wr.sendMessage(msg.to,"ᴀᴜᴛᴏ ɪɴ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    wr.sendMessage(msg.to,"ᴀᴜᴛᴏ ɪɴ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Protectgr"]:
                    wr.sendMessage(msg.to,"「ǫʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    wr.sendMessage(msg.to,"「ǫʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")

                if msg.to in pro["Protectcancl"]:
                    wr.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    wr.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Protectjoin"]:
                    wr.sendMessage(msg.to,"ᴊᴏɪɴᴇᴅ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    wr.sendMessage(msg.to,"ᴊᴏɪɴᴇᴅ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Protectinvite"]:
                    wr.sendMessage(msg.to,"ɪɴᴠɪᴛᴇʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    wr.sendMessage(msg.to,"ɪɴᴠɪᴛᴇʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Autokick"]: 
                    wr.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    wr.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
#=============================================
            elif msg.text in ["Mimic list"]:
                if org["tmimic"] == {}:
                    wr.sendMessage(msg.to,"Not have list")
                else:
                    mc = []
                    for mi_d in org["tmimic"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴍɪᴍɪᴄ ʟɪsᴛ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "Addmimic @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = wr.getGroupIdsJoined()
                    cgroup = wr.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        org['tmimic'][mention['M']] = True
                        wr.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴀᴅᴅᴇᴅ")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
            elif "Unmimic @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = wr.getGroupIdsJoined()
                    cgroup = wr.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        del org['tmimic'][mention['M']]
                        wr.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴅᴇʟᴇᴛᴇᴅ")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
            elif "Mimic " in msg.text:
                xpesan = msg.text
                xres = xpesan.replace("Mimic ","")
                if xres == "off":
                    wait['mimic'] = False
                    wr.sendMessage(msg.to,"ᴍɪᴍɪᴄ sᴇᴛ ᴛᴏ ᴏғғ")
                elif xres == "on":
                    wait['mimic'] = True
                    wr.sendMessage(msg.to,"ᴍɪᴍɪᴄ sᴇᴛ ᴛᴏ ᴏɴ")
            elif "Banned @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in org["Target"]:
                            wr.sendMessage(msg.to,"Already save")
                        elif mention['M']in org["Friend"]:
                            wr.sendMessage(msg.to,"S empty")
                        else:
                            org["Target"][mention['M']] = True
                            with open('setting.json', 'w') as fp:
                                json.dump(wait, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
            elif "Unbanned @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in org["Target"]:
                            del org["Target"][mention['M']]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wr.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴅᴇʟᴇᴛᴇᴅ")
                        else:
                            wr.sendMessage(msg.to,"ᴇᴍᴘᴛʏ ᴛᴀʀɢᴇᴛ")
            elif msg.text in ["Clear ban"]:
                org['Target'] = {}
                with open('org.json', 'w') as fp:
                    json.dump(org, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴄʟᴇᴀʀ")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = yd.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in org["Target"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        wr.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                        return
                    for jj in matched_list:
                        try:
                            wr.kickoutFromGroup(msg.to,[jj])						
                        except:
                            print ("limit")
                    wr.sendMessage(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Add banned"]:
                    wait["atarget"]=True
                    wr.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Del banned"]:
                    wait["dtarget"]=True
                    wr.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Ban list"]:
                if org["Target"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in org["Target"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴛᴀʀɢᴇᴛ ʟɪsᴛ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif msg.text in ["Add silemt"]:
                    wait["asilent"]=True
                    wr.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Del silent"]:
                    wait["dsilent"]=True
                    wr.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Clear silent"]:
                org['Silent'] = {}
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴄʟᴇᴀʀ")
            elif msg.text in ["TBP list"]:
                if org["Silent"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in org["Silent"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴛʙp ʟɪsᴛ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif msg.text in ["Add friend"]:
                    wait["afriend"]=True
                    wr.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Del friend"]:
                    wait["dfriend"]=True
                    wr.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Friend list"]:
                if org["Friend"] == {}:
                    try:
                        wr.sendMessage(msg.to,"ɴᴏ ғʀɪᴇɴᴅ ᴀᴅᴅᴇᴅ")
                    except:
                        pass
                else:
                    mc = []
                    for mi_d in org["Friend"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ Friend List ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif msg.text in ["Clear friend"]:
                org['Friend'] = {}
                with open('org.json', 'w') as fp:
                    json.dump(org, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ғʀɪᴇɴᴅ ᴄʟᴇᴀʀ")
#=============================================
            elif msg.text in ["My grup"]:
                    gid = wr.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = wr.getGroup(i).name
                        h += "╠ ➽ %s\n" % (gn)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴍʏ ɢʀᴜᴘ ⟧\n╔══════════════\n"+ h +"╚══════════════")
#=============================================
            elif "Cname: " in msg.text:
                x = wr.getProfile()
                x.displayName = msg.text.replace("Cname: ","")
                wr.updateProfile(x)
                wr.sendMessage(msg.to, "ᴅᴏɴᴇ")
#=============================================
            elif msg.text in ["Autojoin on"]:
                wait["Autojoin"]=True
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴍᴏᴅᴇ ᴏɴ")
            elif msg.text in ["Autojoin off"]:
                wait["Autojoin"]=False
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴍᴏᴅᴇ ᴏғғ")
#=============================================
            elif msg.text in ["Gift"]:
                    giftnya={'MSGTPL': '5',
                            'PRDTYPE': 'THEME',
                            'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58'}           
                    wr.sendMessage(msg.to,None, contentMetadata=giftnya, contentType=9)
#=============================================
            elif "List grup tikell" == msg.text:
                if resp["grupsticker"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in resp["grupsticker"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ Tikell on ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List prosider" == msg.text:
                if pro["prosider"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["prosider"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘ sɪᴅᴇʀ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List autokick" == msg.text:
                if pro["Autokick"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Autokick"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴀᴜᴛᴏᴋɪᴄᴋ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List auto in" == msg.text:
                if pro["intaPoint"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["intaPoint"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔═════════════\n╠⟦ ᴘotect ᴊᴏɪɴ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List protect join" == msg.text:
                if pro["Protectjoin"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectjoin"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘro ᴊᴏɪɴ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══���═══════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List protect qr" == msg.text:
                if pro["Protectgr"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectgr"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘro ǫʀ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List protect cancel" == msg.text:
                if pro["Protectcancl"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectcancl"]:
                        mc.append(mi_d)
                    pass
                    cban = wr.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘro ᴄᴀɴᴄᴇʟ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
#=============================================
            elif "List protect invite" == msg.text:
                if pro["Protectinvite"] == {}:
                    wr.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectinvite"]:
                        mc.append(mi_d)
                    pass
                    cban = yd.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    wr.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘro ɪɴᴠɪᴛᴇ ɢʀᴜᴘ ⟧\n╔═���════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")

            elif msg.text in ["Tag"]:
                group = wr.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                k = len(nama)//20
                for a in range(k+1):
                    txt = u''
                    s=0
                    b=[]
                    for i in group.members[a*20 : (a+1)*20]:
                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                        s += 7
                        txt += u'@Zero \n'
                    wr.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    
            elif msg.text in ["Cek"]:
                    wr.sendMessage(msg.to, ".")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
            elif msg.text in ["Sider"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        wr.sendMessage(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                      
                    else:
                        wr.sendMessage(msg.to, "ʙᴇʟᴏᴍ ᴅɪ sᴇᴛ ʙᴏsss")
            elif msg.text in ["Sider on"]:
                    pro["prosider"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    wr.sendMessage(msg.to, "sIder ᴍᴏᴅᴇ ᴏɴ ʙᴏs")
                    try:
                        del ciduk['ceadPoint'][msg.to]
                        del ciduk['ceadMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    ciduk['ceadPoint'][msg.to] = msg.id
                    ciduk['ceadMember'][msg.to] = ""
                    ciduk['cetTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    ciduk['cOM'][msg.to] = {}
            elif msg.text in ["Sider off"]:
                    del pro["prosider"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    wr.sendMessage(msg.to, "sIder ᴍᴏᴅᴇ ᴏғғ ʙᴏs")
                    try:
                        del ciduk['ceadPoint'][msg.to]
                        del ciduk['ceadMember'][msg.to]
                    except:
                        pass
#=============================================
            elif msg.text in ["Recover"]:
                thisgroup = wr.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                wr.createGroup("test", mi_d)
                wr.sendMessage(msg.to,"done")
#=============================================
            elif msg.text in ["Hapuschat"]:
                try:
                    wr.removeAllMessages(op.param2)
                    wr.sendMessage(msg.to,"ᴅᴏɴᴇ")
                except:
                    pass
#=============================================
            elif msg.text in ["Wellcome"]:
                gs = wr.getGroup(msg.to)
                wr.sendMessage(msg.to,"ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴏ "+ gs.name)
#=============================================
            elif msg.text in ["Cancel all"]:
                group = wr.getGroup(msg.to)
                if group.invitee is None:
                    wr.sendMessage(op.message.to, "limit")
                else:
                    nama = [contact.mid for contact in group.invitee]
                    for x in nama:
                        time.sleep(0.2)
                        wr.cancelGroupInvitation(msg.to, [x])
                    wr.sendMessage(msg.to, "Berhasil sikat smua pendingan")
#=============================================
            elif msg.text in ["Invite"]:
                    wait["Invi"] = True
                    wr.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
#=============================================
            elif msg.text in ["Member list"]:   
                kontak = wr.getGroup(msg.to)
                group = kontak.members
                msgs="╔══════════════\n╠⟦ ᴍᴇᴍʙᴇʀ ʟɪsᴛ ⟧\n╔══════════════"
                for ids in group:
                    msgs+="\n╠ ➽ %s" % (ids.displayName)
                msgs+="\n╚══════════════\n╠⟦ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs : %i ⟧\n" % len(group)+"╚══════════════"
                wr.sendMessage(msg.to, msgs)

            elif "Cteks comment: " in msg.text:
                wira["comment"] = msg.text.replace("Cteks comment: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(wira, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Comment teks"]:
                wr.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + wira["comment"])
#=============================================
            elif "Cteks cctv: " in msg.text:
                wira["cctvteks"] = msg.text.replace("Cteks cctv: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(wira, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Cctv teks"]:
                wr.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + wira["cctvteks"])
#=============================================
            elif "Cteks tag1: " in msg.text:
                wira["tagteks1"] = msg.text.replace("Cteks tag1: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(wira, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")
#=============================================
            elif "Cteks tag2: " in msg.text:
                wira["tagteks2"] = msg.text.replace("Cteks tag2: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(wira, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")
#=============================================
            elif "Cteks left: " in msg.text:
                wira["leftmsg"] = msg.text.replace("Cteks left: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(wira, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Left teks"]:
                wr.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + wira["leftmsg"])
#=============================================
            elif "Cteks wellcome: " in msg.text:
                wira["welmsg"] = msg.text.replace("Cteks wellcome: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(wira, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Wellcome teks"]:
                wr.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + wira["welmsg"])   
#=============================================
            elif "Cteks add: " in msg.text:
                wira["message"] = msg.text.replace("Cteks add: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(wira, fp, sort_keys=True, indent=4)
                wr.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Add teks"]:
                wr.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + wira["message"])
#=============================================
        if op.type == 26:
            msg = op.message
            if msg.toType == 2:
                if wait["mimic"] == True:
                    if msg.from_ in wait["tmimic"]:
                        text = msg.text
                        if text in helpMessage:
                            pass
                        elif text in helpMessage1:
                            pass
                        elif text in helpMessage2:
                            pass
                        elif text in helpMessage3:
                            pass
                        else:
                            wr.sendMessage(msg.to,text)
                    else:
                        pass
                else:
                    pass

            if msg.toType == 2:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if resp["Tag1"] == True:    
                        contact = wr.getContact(msg._from)
                        cName = contact.displayName
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if mention['M'] in wrMID:
                                wr.sendMessage(msg.to,"ᴴᴬᵞ @!"+cName+"\n"+wira["tagteks1"])
                                wr.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+contact.pictureStatus)
                                rnd = ["Jangan tag tar syang"]
                                p = random.choice(rnd)
                                lang = 'id'
                                tts = gTTS(text=p, lang=lang)
                                tts.save("hasil.mp3")
                                wr.sendAudio(msg.to,"hasil.mp3")
                                break
                    else:
                        pass
                    if resp["Tag2"] == True:          
                        contact = wr.getContact(msg._from)
                        cName = contact.displayName
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if mention['M'] in wrMID:
                                wr.sendMessage(msg.to,cName+"\n"+wira["tagteks2"])   
                                break
                    else:
                        pass
    except Exception as error:
        logError(error)
#==============================================================================#

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                wiraBot(op)
                # jangan di hapus bagian  wira, byar tidak terjadi troblle!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)