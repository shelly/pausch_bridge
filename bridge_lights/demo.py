import lumiversepython as L
import time

rig = L.Rig("/home/teacher/Lumiverse/PBridge.rig.json")
rig.init()

sent = "hi hi hi hi hi hi hi hi hi hi"
sent2 = "hello hello hello hello hello"
color = (209, 91, 252)
color2 = (252, 91, 123)

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

    # play animation of text from gates
    idx = 0
    while(idx < 60):
        if (idx < len(s1) and s1[idx] != " "):
            rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0.5, 0, 0)
            rig.updateOnce()
            time.sleep(0.1)
        idx = idx + 1

    # play animation of text from purnell
    idx = 0
    while(idx < 60):
        if (idx < len(s2) and s2[idx] != " "):
            rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 1)
            rig.updateOnce()
            time.sleep(0.2)
        idx = idx + 1
    time.sleep(0.5)

    # # fade out
    # idx = 5
    # while(idx >= 0):
    #     if (idx < len(s1) and s1[idx] != " "):
    #         rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw((color[0] * idx * 0.2), (color[1] * idx * 0.2), (color[2] * idx * 0.2))
    #         rig.updateOnce()
    #         time.sleep(0.1)
    #     if (idx < len(s2) and s2[idx] != " "):
    #         rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw((color[0] * idx * 0.2), (color[1] * idx * 0.2), (color[2] * idx * 0.2))
    #         rig.updateOnce()
    #         time.sleep(0.1)
    #     idx = idx - 1

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

updateText("top", "aaaa ooo aaaa ooo ooo aaaa a a a aa a", (209, 91, 252))
