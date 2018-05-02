import lumiversepython as L
import time

rig = L.Rig("/home/teacher/Lumiverse/PBridge.rig.json")
rig.init()

sent = "hi hi hi hi hi hi hi hi hi hi"
sent2 = "hello hello hello hello hello ooo oooo"
color = (0.82, 0.45, 0.98)
color2 = (1,.7,.11)

def playText(s1, s2, color, color2):
    # play animation of text from gates
    idx = 0
    while(idx < 60):
        if (idx < len(s1) and s1[idx] != " "):
            rig.select("$side=top[$panel=" + str(idx+1) + "]").setRGBRaw(color[0], color[1], color[2])
            rig.updateOnce()
            time.sleep(0.2)
        idx = idx + 1

    # play animation of text from purnell
    idx = 0
    while(idx < 60):
        if (idx < len(s2) and s2[idx] != " "):
            rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(color2[0], color2[1], color2[2])
            rig.updateOnce()
            time.sleep(0.3)
        idx = idx + 1
    time.sleep(3)

def getColor(color):
    c = (0.5, 0.5, 0.5 )
    side = '' 

    if color == 'light_pink':
        c = (.98,.35,.48)
        side = 'bot'
    elif color == 'orange':
        c = (1,.7,.11)
        side = 'bot'
    elif color == 'yellow':
        c = (0.8,.78,.1)
        side = 'bot'
    elif color == 'bright_pink':
        c = (.98,.35,.73)
        side = 'bot'
    elif color == 'purple':
        c = (0.82, 0.45, 0.98)
        side = 'top' 
    elif color == 'violet':
        c = (0.48, 0.36, 0.9)
        side = 'top'
    elif color == 'blue':
        c = (0.06, 0.27, 0.8)
        side = 'top'
    else: # teal 
        c = (0.24, 0.9, 0.95)
        side = 'top'

    return c, side

def playShow():       
    s1 = sent + ((60 - len(sent)) * " ")
    s2 = sent2 + ((60 - len(sent2)) * " ")
    print ("sent is " + str(len(s1)) + ", sent2 is " + str(len(s2)))

    playText(s1, s2, color, color2)

    # # fade out
    # idx = 0
    # idx2 = 5
    # while(idx2 >= 0):
    #     while (idx < 60):
    #         if (idx < len(s1) and s1[idx] != " "):
    #             rig.select("$side=top[$panel=" + str(idx+1) + "]").setIntensity(idx2 * 20)
    #         if (idx < len(s2) and s2[idx] != " "):
    #             rig.select("$side=bot[$panel=" + str(60-idx) + "]").setIntensity(idx2 * 20)
    #         idx = idx + 1
    #     rig.updateOnce()
    #     time.sleep(0.2)
    #     idx2 = idx2 - 1

    # turn everything off
    idx = 0
    while (idx < 60):
      rig.select("$side=top[$panel=" + str(idx+1) + "]").setRGBRaw(0, 0, 0)
      rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 0)
      idx = idx + 1
    rig.updateOnce()
    time.sleep(0.1)

    # turn space spots white
    idx = 0
    while (idx < 60):
        if (s1[idx] == " " and s2[59-idx] == " "):
            rig.select("$side=top[$panel=" + str(idx+1) + "]").setRGBRaw(1, 1, 1)
            rig.select("$side=bot[$panel=" + str(idx+1) + "]").setRGBRaw(1, 1, 1)
        idx = idx + 1
    rig.updateOnce()
    time.sleep(3)

    # turn off white
    idx = 0
    while (idx < 60):
        if (s1[idx] == " " and s2[59-idx] == " "):
            rig.select("$side=top[$panel=" + str(idx+1) + "]").setRGBRaw(0, 0, 0)
            rig.select("$side=bot[$panel=" + str(idx+1) + "]").setRGBRaw(0, 0, 0)
        idx = idx + 1

    rig.updateOnce()
    time.sleep(1)

    playText(s1, s2, color, color2)
    
def updateText(text, c):
    print "UPDATING TEXT"
    global sent, sent2, color, color2

    co, side = getColor(c)

    if side == "top":
        sent = text
        color = co
    else:
        sent2 = text
        color2 = co

    playShow()
