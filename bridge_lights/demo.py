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
            rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(color[0], color[1], color[2])
            rig.updateOnce()
            time.sleep(0.1)
        idx = idx + 1

    # play animation of text from purnell
    idx = 0
    while(idx < 60):
        if (idx < len(s2) and s2[idx] != " "):
            rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(color2[0], color2[1], color2[2])
            rig.updateOnce()
            time.sleep(0.2)
        idx = idx + 1
    time.sleep(0.5)

# loc: top or bot
def updateText(loc, text, c):
    global sent, sent2, color, color2
    if not (loc == "top" or loc == "bottom"):
        print "not valid loc"
        return

    if loc == "top":
        sent = text
        color = c
    else:
        sent2 = text
        color2 = c

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
    #             rig.select("$side=top[$panel=" + str(idx) + "]").setIntensity(idx2 * 0.2)
    #         if (idx < len(s2) and s2[idx] != " "):
    #             rig.select("$side=bot[$panel=" + str(60-idx) + "]").setIntensity(idx2 * 0.2)
    #         idx = idx + 1
    #     rig.updateOnce()
    #     time.sleep(0.1)
    #     idx2 = idx2 - 1

    # turn everything off
    idx = 0
    while (idx < 60):
      rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0)
      rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 0)
      idx = idx + 1
    rig.updateOnce()
    time.sleep(0.3)

    # turn space spots white
    idx = 0
    if (len(s1) + len(s2) < 60):
        print "HERE"
        idx2 = len(s1)
        while (idx2 < 60 - len(s2)):
            rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
            rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
            idx2 = idx2 + 1
    else:
        while (idx < 60):
            if (s1[idx] == " " and s2[59-idx] == " "):
                rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
                rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
            idx = idx + 1

    rig.updateOnce()
    time.sleep(0.2)

    playText(s1, s2, color, color2)

updateText("top", "aaaa ooo aaaa ooo ooo aaaa a a a aa a", (0.82, 0.45, 0.98))
